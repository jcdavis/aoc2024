import argparse
from collections import defaultdict

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    left = []
    right = {}
    with open(args.file) as file:
        for line in file:
            parts = line.strip().split()
            left.append(int(parts[0]))
            rightNum = int(parts[1])
            right[rightNum] = right.get(rightNum, 0) + 1

    diff = 0
    for i in range(0, len(left)):
        diff += left[i]*right.get(left[i], 0)

    print(diff)

if __name__ == "__main__":
    main()