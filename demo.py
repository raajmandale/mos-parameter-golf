from infer import CRSEngine


def main() -> None:
    engine = CRSEngine()

    print("CRS-Core Demo")
    print("Modes shown: baseline, raw, crs, noisy")
    print("Type a query. Press Ctrl+C to exit.\n")

    while True:
        query = input(">> ").strip()
        if not query:
            continue

        baseline = engine.predict(query, mode="baseline")
        raw = engine.predict(query, mode="raw")
        crs = engine.predict(query, mode="crs")
        noisy = engine.predict(query, mode="noisy")

        print("\n--- Baseline ---")
        print(f"Prediction: {baseline['prediction']}")

        print("\n--- Raw Retrieved Context ---")
        print(f"Context   : {raw['context']}")
        print(f"Prediction: {raw['prediction']}")

        print("\n--- CRS (Scored Context) ---")
        print(f"Context   : {crs['context']}")
        print(f"Prediction: {crs['prediction']}")

        print("\n--- Noisy Context ---")
        print(f"Context   : {noisy['context']}")
        print(f"Prediction: {noisy['prediction']}\n")


if __name__ == "__main__":
    main()