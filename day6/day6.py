import argparse

directions = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def is_loop(map: list[str], x: int, y: int) -> bool:
    visited = set()
    dir = 0
    while True:
        if (x,y,dir) in visited:
            return True
        visited.add((x,y, dir))
        (dx, dy) = directions[dir]
        next_x = x + dx
        next_y = y + dy
        if next_x >= 0 and next_x < len(map[0]) and next_y >= 0 and next_y < len(map):
            if map[next_y][next_x] == '#':
                dir = (dir+1)%4
            else:
                x = next_x
                y = next_y
        else:
            return False

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    lines = []
    start_x = -1
    start_y = -1
    with open(args.file) as file:
        for line in file:
            idx = line.find('^')
            if idx != -1:
                start_x = idx
                start_y = len(lines)
            lines.append(line.strip())

    print(f'Starting at ({start_x}, {start_y})')

    loops = 0
    for x in range(0, len(lines[0])):
        for y in range(0, len(lines)):
            if lines[y][x] == '.':
                old = lines[y]
                lines[y] = old[:x] + '#' + old[x+1:]
                if is_loop(lines, start_x, start_y):
                    loops += 1
                lines[y] = old

    print(loops)

if __name__ == "__main__":
    main()