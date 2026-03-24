from pathlib import Path

import torch
import torch.nn as nn
import torch.optim as optim

from model.tiny_lm import TinyLM
from model.vocab import Vocab
from model.utils import load_json, pad_batch, set_seed
from crs.retriever import Retriever
from crs.scorer import score_matches
from crs.builder import build_context


USE_CRS_TRAINING = True
MODEL_PATH = "tiny_model.pt"
VOCAB_PATH = "model/vocab.json"


def build_input_text(query: str, retriever: Retriever) -> str:
    if not USE_CRS_TRAINING:
        return query

    matches = retriever.retrieve(query)
    scored = score_matches(query, matches)
    context = build_context(scored, top_k=2)
    if context:
        return f"{query} {context}"
    return query


def main() -> None:
    set_seed(42)

    train_data = load_json("data/train_samples.json")
    vocab = Vocab.build_from_datasets(["data/train_samples.json", "data/test_samples.json"])
    vocab.save(VOCAB_PATH)

    retriever = Retriever()

    input_sequences = []
    target_ids = []

    for row in train_data:
        input_text = build_input_text(row["query"], retriever)
        input_sequences.append(vocab.encode(input_text))
        target_ids.append(vocab.encode(row["answer"])[0])

    x = pad_batch(input_sequences, vocab.pad_id)
    y = torch.tensor(target_ids, dtype=torch.long)

    model = TinyLM(vocab_size=vocab.size, embed_dim=64, hidden_dim=64)
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    loss_fn = nn.CrossEntropyLoss()

    epochs = 300
    model.train()

    for epoch in range(epochs):
        logits = model(x)
        loss = loss_fn(logits, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 50 == 0 or epoch == epochs - 1:
            pred = torch.argmax(logits, dim=1)
            acc = (pred == y).float().mean().item()
            print(f"epoch={epoch:03d} loss={loss.item():.4f} acc={acc:.2%}")

    torch.save(model.state_dict(), MODEL_PATH)
    print(f"\nSaved model to: {MODEL_PATH}")
    print(f"Saved vocab to: {VOCAB_PATH}")


if __name__ == "__main__":
    main()