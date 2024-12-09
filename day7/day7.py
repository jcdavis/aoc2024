import argparse
import re

def can_equal(current: int, target: int, parts: list[int], i: int) -> bool:
    if i == len(parts):
        return current == target
    if current > target:
        # Short-circuit if we can't possibly hit target
        return False
    return can_equal(current + parts[i], target, parts, i+1) or can_equal(
        current*parts[i], target, parts, i+1
    ) or can_equal(
        int(f'{current}{parts[i]}'), target, parts, i+1
    )

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    totals = 0
    regex = re.compile(r'(\d+): (\d.+)')
    with open(args.file) as file:
        rule = True
        for line in file:
            stripped = line.strip()
            matched = regex.match(stripped)
            left = int(matched.group(1))
            right = [int(p) for p in matched.group(2).split()]
            if can_equal(right[0], left, right, 1):
                totals += left

    print(totals)

if __name__ == "__main__":
    main()