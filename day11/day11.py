import argparse

def blink(stones: dict[int, int]) -> dict[int, int]:
    result = {}

    for stone, count in stones.items():
        if stone == 0:
            result[1] = result.get(1, 0) + count
        else:
            as_str = str(stone)
            if len(as_str) % 2 == 0:
                left = int(as_str[:len(as_str)>>1])
                result[left] = result.get(left, 0) + count
                right = int(as_str[len(as_str)>>1:])
                result[right] = result.get(right, 0) + count
            else:
                result[2024*stone] = result.get(2024*stone, 0) + count

    return result

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file) as file:
        line = next(file)
        stones = {}
        for n in line.split():
            as_int = int(n)
            stones[as_int] = stones.get(as_int, 0) + 1

        for i in range(75):
            stones = blink(stones)

        total = 0
        for c in stones.values():
            total += c
        print(total)




if __name__ == "__main__":
    main()