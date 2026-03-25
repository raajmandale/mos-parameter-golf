import os
import re
import subprocess
import sys

def run_case(use_crs: bool, keep_ratio: float):
    print("\n==============================")
    print(f"Running with USE_CRS={use_crs}, KEEP_RATIO={keep_ratio}")
    print("==============================")

    env = os.environ.copy()
    env["USE_CRS"] = "True" if use_crs else "False"
    env["KEEP_RATIO"] = str(keep_ratio)

    result = subprocess.run(
        [sys.executable, "train.py"],
        env=env,
        check=True,
        capture_output=True,
        text=True
    )

    print(result.stdout)

    raw_tokens = extract_int(result.stdout, r"raw_tokens=(\d+)")
    final_tokens = extract_int(result.stdout, r"final_tokens=(\d+)")
    final_loss = extract_float(result.stdout, r"final_loss=([0-9.]+)")
    train_time = extract_float(result.stdout, r"train_time_sec=([0-9.]+)")

    return {
        "use_crs": use_crs,
        "keep_ratio": keep_ratio,
        "raw_tokens": raw_tokens,
        "final_tokens": final_tokens,
        "final_loss": final_loss,
        "train_time_sec": train_time,
    }

def extract_int(text: str, pattern: str) -> int:
    m = re.search(pattern, text)
    if not m:
        raise ValueError(f"Could not find int for pattern: {pattern}")
    return int(m.group(1))

def extract_float(text: str, pattern: str) -> float:
    m = re.search(pattern, text)
    if not m:
        raise ValueError(f"Could not find float for pattern: {pattern}")
    return float(m.group(1))

if __name__ == "__main__":
    results = []

    results.append(run_case(False, 1.0))
    for ratio in [0.85, 0.75, 0.60]:
        results.append(run_case(True, ratio))

    print("\n==============================================")
    print("CRS Controlled Sweep Summary")
    print("==============================================")
    print(f"{'Mode':<12} {'Ratio':<8} {'Raw':<6} {'Final':<6} {'Loss':<10} {'Time(s)':<10}")
    print("----------------------------------------------")

    for r in results:
        mode = "baseline" if not r["use_crs"] else "crs"
        print(
            f"{mode:<12} "
            f"{r['keep_ratio']:<8.2f} "
            f"{r['raw_tokens']:<6} "
            f"{r['final_tokens']:<6} "
            f"{r['final_loss']:<10.4f} "
            f"{r['train_time_sec']:<10.4f}"
        )

    print("==============================================")
