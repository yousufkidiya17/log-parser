"""Simple log parser"""
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
