import argparse

map: list[str] = []
visited: set[(int, int)] = set()

# Represent edge pieces as elements with the square and delta for direction
def recurse(x: int , y: int, px: int, py: int, expected: str) -> tuple[int, set[tuple[int, int, int, int]]]:
    if x < 0 or x >= len(map[0]) or y < 0 or y >= len(map) or map[y][x] != expected:
        # count new perimeter
        dx = x - px
        dy = y - py
        return (0, {(px, py, dx, dy)})
    if (x,y) in visited:
        # Already visited this square as part of counting this letter
        return (0, set())
    visited.add((x,y))

    (left_area, left_perim) = recurse(x-1, y, x, y, expected)
    (right_area, right_perim) = recurse(x+1, y, x, y, expected)
    (up_area, up_perim) = recurse(x, y-1, x, y, expected)
    (down_area, down_perim) = recurse(x, y+1, x, y, expected)

    area = 1 + left_area + right_area + up_area + down_area
    perimeter = left_perim.union(right_perim).union(up_perim).union(down_perim)
    return (area, perimeter)

# Given a set of edge pieces, count sides by walking directions
def count_sides(edges: set[tuple[int, int, int, int]]) -> int:
    sides = 0
    while len(edges) > 0:
        edge = next(iter(edges))
        sides += 1
        edges.remove(edge)
        (x, y, ex, ey) = edge
        dx = 1 if ey != 0 else 0
        dy = 1 if ex != 0 else 0
        # Now iterate in both directions removing attached edge pieces
        sx = x + dx
        sy = y + dy
        while (sx, sy, ex, ey) in edges:
            edges.remove((sx, sy, ex, ey))
            sx += dx
            sy += dy
        # Now other way
        sx = x - dx
        sy = y - dy
        while (sx, sy, ex, ey) in edges:
            edges.remove((sx, sy, ex, ey))
            sx -= dx
            sy -= dy

    return sides

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file) as file:
        for line in file:
            map.append(line.strip())

    total = 0
    for x in range(len(map[0])):
        for y in range(len(map)):
            # First square will never be out of region so fine if px/py are dummy
            (area, perimeter) = recurse(x, y, x, y, map[y][x])
            if area > 0:
                edges = count_sides(perimeter)
                print(f'({x},{y}): {area}*{edges}')
                total += area*edges

    print(total)


if __name__ == "__main__":
    main()