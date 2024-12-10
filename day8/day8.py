import argparse
from collections import defaultdict

positions = defaultdict(list)
antinodes = set()
map = []

def insert_if_valid(p1: tuple[int, int], p2: tuple[int, int]) -> None:
     dx = p1[0] - p2[0]
     dy = p1[1] - p2[1]
     nx = p1[0]
     ny = p1[1]

     while nx >= 0 and nx < len(map[0]) and ny >= 0 and ny < len(map):
          antinodes.add((nx, ny))
          nx += dx
          ny += dy

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file) as file:
        for line in file:
            map.append(line.strip())

    for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] != '.':
                    positions[map[y][x]].append((x, y))
            y += 1

    for pairs in positions.values():
         for i in range(len(pairs)):
              for j in range(0, i):
                   p1 = pairs[i]
                   p2 = pairs[j]
                   insert_if_valid(p1, p2)
                   insert_if_valid(p2, p1)

    print(len(antinodes))
if __name__ == "__main__":
    main()