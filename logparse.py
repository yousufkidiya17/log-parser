"""Simple log parser"""
import sys
from collections import Counter

def summarize(path):
    levels = Counter()
    with open(path, encoding="utf-8", errors="ignore") as f:
        for line in f:
            for lvl in ("INFO", "WARN", "ERROR", "DEBUG"):
                if lvl in line:
                    levels[lvl] += 1
                    break
    for lvl, n in levels.most_common():
        print(f"{lvl}: {n}")

def errors(path, out):
    with open(path, encoding="utf-8", errors="ignore") as f, open(out, "w", encoding="utf-8") as o:
        for line in f:
            if "ERROR" in line:
                o.write(line)
    print(f"errors -> {out}")

if __name__ == "__main__":
    if sys.argv[1] == "summary":
        summarize(sys.argv[2])
    else:
        errors(sys.argv[2], sys.argv[3])
