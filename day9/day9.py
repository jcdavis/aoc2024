import argparse
from typing import Optional

blocks: list[int] = []

def next_free(start: int) -> Optional[int]:
    for i in range(start, len(blocks)):
        if blocks[i] == -1:
            return i
    return None

def next_fill(start: int) -> Optional[int]:
    for i in range(start, 0, -1):
        if blocks[i] != -1:
            return i
    return None

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    next_block_num = 0

    with open(args.file) as file:
        line = next(file).strip()
        for i in range(len(line)):
            if i%2 == 0:
                if line[i] == 0:
                    print("HOW TO HANDLE ZERO FILE BLOCKS???")
                for _ in range(int(line[i])):
                    blocks.append(next_block_num)
                next_block_num += 1
            else:
                for _ in range(int(line[i])):
                    blocks.append(-1)

    current_free = next_free(0)
    fill_from = next_fill(len(blocks) - 1)

    # print(f'{current_free} - {fill_from}')
    while current_free < fill_from:
        # print(f'Moving {blocks[current_free]} {current_free} - {fill_from}')
        blocks[current_free] = blocks[fill_from]
        blocks[fill_from] = -1
        current_free = next_free(current_free + 1)
        fill_from = next_fill(fill_from - 1)

    # print(blocks)
    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != -1:
            checksum += i*blocks[i]

    print(checksum)

if __name__ == "__main__":
    main()