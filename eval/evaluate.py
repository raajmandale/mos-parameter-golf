import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from infer import CRSEngine
from model.utils import load_json


def evaluate_mode(mode: str) -> float:
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
    baseline_acc = evaluate_mode("baseline")
    raw_acc = evaluate_mode("raw")
    crs_acc = evaluate_mode("crs")
    noisy_acc = evaluate_mode("noisy")

    print("\n==============================")
    print("CRS-Core Evaluation Report")
    print("==============================\n")
    print(f"Baseline Accuracy : {baseline_acc:.2%}")
    print(f"Raw Context Acc   : {raw_acc:.2%}")
    print(f"CRS Accuracy      : {crs_acc:.2%}")
    print(f"Noisy Context Acc : {noisy_acc:.2%}")
    print(f"\nCRS Improvement   : {(crs_acc - baseline_acc):.2%}")
    print("==============================\n")


if __name__ == "__main__":
    main()