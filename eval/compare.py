import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from infer import CRSEngine
from model.utils import load_json


def main() -> None:
    engine = CRSEngine()
    test_data = load_json("data/test_samples.json")

    print("CRS Comparison Report\n")

    counts = {
        "baseline": 0,
        "raw": 0,
        "crs": 0,
        "noisy": 0,
    }

    total = len(test_data)

    for row in test_data:
        query = row["query"]
        gold = row["answer"].strip().lower()

        baseline = engine.predict(query, mode="baseline")
        raw = engine.predict(query, mode="raw")
        crs = engine.predict(query, mode="crs")
        noisy = engine.predict(query, mode="noisy")

        baseline_ok = baseline["prediction"].strip().lower() == gold
        raw_ok = raw["prediction"].strip().lower() == gold
        crs_ok = crs["prediction"].strip().lower() == gold
        noisy_ok = noisy["prediction"].strip().lower() == gold

        counts["baseline"] += int(baseline_ok)
        counts["raw"] += int(raw_ok)
        counts["crs"] += int(crs_ok)
        counts["noisy"] += int(noisy_ok)

        print(f"Q: {query}")
        print(f"Gold       : {gold}")
        print(f"Baseline   : {baseline['prediction']}   [{'OK' if baseline_ok else 'MISS'}]")
        print(f"Raw Context: {raw['context']}")
        print(f"Raw Output : {raw['prediction']}   [{'OK' if raw_ok else 'MISS'}]")
        print(f"CRS Context: {crs['context']}")
        print(f"CRS Output : {crs['prediction']}   [{'OK' if crs_ok else 'MISS'}]")
        print(f"Noisy Ctx  : {noisy['context']}")
        print(f"Noisy Out  : {noisy['prediction']}   [{'OK' if noisy_ok else 'MISS'}]")
        print("-" * 60)

    print("\n==============================")
    print("Final Accuracy Summary")
    print("==============================")
    print(f"Baseline : {counts['baseline'] / total:.2%}")
    print(f"Raw      : {counts['raw'] / total:.2%}")
    print(f"CRS      : {counts['crs'] / total:.2%}")
    print(f"Noisy    : {counts['noisy'] / total:.2%}")
    print("==============================\n")


if __name__ == "__main__":
    main()