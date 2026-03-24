import torch

from model.tiny_lm import TinyLM
from model.vocab import Vocab
from model.utils import pad_batch
from crs.retriever import Retriever
from crs.scorer import score_matches
from crs.builder import build_context


MODEL_PATH = "tiny_model.pt"
VOCAB_PATH = "model/vocab.json"


class CRSEngine:
    def __init__(self):
        self.vocab = Vocab.load(VOCAB_PATH)
        self.model = TinyLM(vocab_size=self.vocab.size, embed_dim=64, hidden_dim=64)
        self.model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
        self.model.eval()
        self.retriever = Retriever()

    def build_good_context(self, query: str) -> str:
        matches = self.retriever.retrieve(query)
        scored = score_matches(query, matches)
        return build_context(scored, top_k=2)

    def build_raw_context(self, query: str) -> str:
        matches = self.retriever.retrieve(query)
        raw = []
        for item in matches[:2]:
            raw.append(f"{item['entity']} {item['relation']} {item['value']}")
        return " ".join(raw).strip()

    def build_bad_context(self) -> str:
        return "germany capital berlin hamlet author shakespeare"

    def predict(self, query: str, mode: str = "crs") -> dict:
        """
        Modes:
        - baseline: query only
        - raw: query + raw retrieved context
        - crs: query + scored compact context
        - noisy: query + bad context
        """
        context = ""

        if mode == "baseline":
            input_text = query
        elif mode == "raw":
            context = self.build_raw_context(query)
            input_text = f"{query} {context}".strip() if context else query
        elif mode == "noisy":
            context = self.build_bad_context()
            input_text = f"{query} {context}".strip()
        else:
            context = self.build_good_context(query)
            input_text = f"{query} {context}".strip() if context else query

        encoded = self.vocab.encode(input_text)
        x = pad_batch([encoded], self.vocab.pad_id)

        with torch.no_grad():
            logits = self.model(x)
            pred_id = torch.argmax(logits, dim=1).item()

        answer = self.vocab.decode_id(pred_id)

        return {
            "query": query,
            "mode": mode,
            "context": context,
            "prediction": answer,
        }


if __name__ == "__main__":
    engine = CRSEngine()
    for mode in ["baseline", "raw", "crs", "noisy"]:
        result = engine.predict("what is capital of france", mode=mode)
        print(result)