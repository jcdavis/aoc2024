import argparse
from typing import Optional

heights: list[list[int]] = []

def count_paths(x: int, y: int, expected: int) -> int:
    if x < 0 or x >= len(heights[0]) or y < 0 or y >= len(heights):
        return 0
    if heights[y][x] != expected:
        return 0
    # Must be expected
    if heights[y][x] == 9:
        return 1
    return count_paths(x-1, y, expected+1) + count_paths(x+1, y, expected+1) + count_paths(
        x, y-1, expected+1
    ) + count_paths(x, y+1, expected+1)

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file) as file:
        for line in file:
            heights.append([int(x) for x in line.strip()])

    totals = 0

    for x in range(0, len(heights[0])):
        for y in range(0, len(heights)):
            result = count_paths(x, y, 0)
            if result > 0 :
                print(f'Found {result} at ({x},{y})')
            totals += result

    print(totals)

if __name__ == "__main__":
    main()