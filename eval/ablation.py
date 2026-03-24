import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from infer import CRSEngine
from model.utils import load_json


def evaluate(mode: str) -> float:
    engine = CRSEngine()
    test_data = load_json("data/test_samples.json")

    correct = 0
    total = len(test_data)

    for row in test_data:
        result = engine.predict(row["query"], mode=mode)
        pred = result["prediction"].strip().lower()
        gold = row["answer"].strip().lower()
        if pred == gold:
            correct += 1

    return correct / total if total else 0.0


def main() -> None:
    baseline = evaluate("baseline")
    raw = evaluate("raw")
    crs = evaluate("crs")

    print("\n==============================")
    print("CRS-Core Ablation Study")
    print("==============================\n")
    print(f"1. TinyLM only              : {baseline:.2%}")
    print(f"2. TinyLM + raw retrieval   : {raw:.2%}")
    print(f"3. TinyLM + scored CRS      : {crs:.2%}")
    print("\nInterpretation:")
    print("- baseline tests model alone")
    print("- raw retrieval tests unfiltered context")
    print("- CRS tests scored compact reconstruction")
    print("==============================\n")


if __name__ == "__main__":
    main()