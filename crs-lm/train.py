import os
import time
import torch
import torch.nn as nn
import torch.optim as optim

from model.tokenizer import Tokenizer
from model.tiny_lm import TinyLM
from crs.filter import crs_filter

with open("data/tiny_corpus.txt", "r", encoding="utf-8") as f:
    text = f.read().strip()

tok = Tokenizer()
tok.fit(text)

raw_tokens = tok.encode(text)
tokens = raw_tokens[:]

use_crs = os.getenv("USE_CRS", "True") == "True"
keep_ratio = float(os.getenv("KEEP_RATIO", "0.75"))

if use_crs:
    tokens = crs_filter(tokens, tok.idx2word, keep_ratio=keep_ratio)

print(
    f"raw_tokens={len(raw_tokens)}, "
    f"final_tokens={len(tokens)}, "
    f"use_crs={use_crs}, "
    f"keep_ratio={keep_ratio}"
)

seq_len = 4
X, Y = [], []

for i in range(len(tokens) - seq_len):
    X.append(tokens[i:i + seq_len])
    Y.append(tokens[i + 1:i + seq_len + 1])

if not X:
    raise ValueError("Not enough tokens after CRS filtering. Increase corpus size or keep_ratio.")

X = torch.tensor(X, dtype=torch.long)
Y = torch.tensor(Y, dtype=torch.long)

model = TinyLM(vocab_size=len(tok.word2idx))
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

start = time.time()

for epoch in range(201):
    optimizer.zero_grad()
    logits = model(X)
    loss = criterion(logits.view(-1, logits.size(-1)), Y.view(-1))
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(
            f"epoch={epoch}, loss={loss.item():.4f}, "
            f"use_crs={use_crs}, keep_ratio={keep_ratio}"
        )

elapsed = time.time() - start
print(f"final_loss={loss.item():.4f}")
print(f"train_time_sec={elapsed:.4f}")
print("done")
