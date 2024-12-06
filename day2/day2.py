import argparse
from collections import defaultdict

def is_safe(report: list[int]) -> bool:
    increasing = False
    decreasing = False
    for i in range(1, len(report)):
        diff = report[i] - report[i-1]
        if diff == 0 or abs(diff) > 3:
            return False
        if diff > 0:
            increasing = True
        else:
            decreasing = True
        if increasing and decreasing:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()

    safe = 0
    with open(args.file) as file:
        for line in file:
            parts = [int(x) for x in line.strip().split()]
            if is_safe(parts):
                safe += 1
            else:
                for i in range(0, len(parts)):
                    cloned = parts.copy()
                    cloned.pop(i)
                    if is_safe(cloned):
                        safe += 1
                        break



    print(safe)

if __name__ == "__main__":
    main()