import argparse

target = 'XMAS'

def count_direction(map: list[str], x: int, y: int, dx: int, dy: int) -> int:
    seen = 0
    position = 0
    startx = x
    starty = y
    while x >= 0 and y >= 0 and x < len(map[0]) and y < len(map):
        # print(f'At ({x},{y}): {map[y][x]}')
        if map[y][x] == target[position]:
            position += 1
            if position == len(target):
                seen += 1
                position = 0
                print(f'{startx},{starty} - {x},{y}')
                startx = x
                starty = y
        else:
            # print('Mismatch, reset')
            if map[y][x] == 'X':
                position = 1
            else:
                position = 0
            startx = x
            starty = y
        x += dx
        y += dy
    return seen

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    lines = []
    with open(args.file) as file:
        for line in file:
            lines.append(line.strip())

    seen = 0
    end_x = len(lines[0])
    end_y = len(lines)

    for x in range(1, end_x-1):
        for y in range(1, end_y-1):
            if lines[y][x] == 'A':
                diag = (lines[y-1][x-1] == 'M' and lines[y+1][x+1] == 'S') or (
                    lines[y-1][x-1] == 'S' and lines[y+1][x+1] == 'M')
                reverse_diag = (lines[y-1][x+1] == 'M' and lines[y+1][x-1] == 'S') or (
                    lines[y-1][x+1] == 'S' and lines[y+1][x-1] == 'M')
                if diag and reverse_diag:
                    seen += 1

    print(seen)


if __name__ == "__main__":
    main()