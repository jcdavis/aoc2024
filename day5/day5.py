import argparse
from collections import defaultdict
from functools import cmp_to_key

is_before = defaultdict(set)

def is_valid(parts: list[str]) -> bool:
    for i in range(1, len(parts)):
        for j in range(0, i):
            if parts[i] in is_before[parts[j]]:
                return False
    return True

def compare(left: str, right: str) -> int:
    if left in is_before[right]:
        return -1
    if right in is_before[left]:
        return 1
    return 0

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    totals = 0
    with open(args.file) as file:
        rule = True
        for line in file:
            stripped = line.strip()
            if not stripped:
                rule = False
                continue
            if rule:
                parts = stripped.split("|")
                is_before[parts[1]].add(parts[0])
            else:
                parts = stripped.split(",")
                if not is_valid(parts):
                    parts = sorted(parts, key=cmp_to_key(compare))
                    totals += int(parts[len(parts)>>1])

    print(totals)

if __name__ == "__main__":
    main()