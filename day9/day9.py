import argparse
from typing import Optional

blocks: list[int] = []
block_map: list[(int, int)] = []

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    next_block_num = 0

    with open(args.file) as file:
        line = next(file).strip()
        for i in range(len(line)):
            length = int(line[i])
            if i%2 == 0:
                if line[i] == 0:
                    print("HOW TO HANDLE ZERO FILE BLOCKS???")
                block_map.append((len(blocks), length))
                for _ in range(length):
                    blocks.append(next_block_num)
                next_block_num += 1
            else:
                for _ in range(length):
                    blocks.append(-1)

    for i in reversed(range(0, len(block_map))):
        (start, length) = block_map[i];

        for j in range(0, start):
            is_empty = True
            for k in range(j, j+length):
                if blocks[k] != -1:
                    is_empty = False
            if is_empty:
                for k in range(0, length):
                    blocks[j+k] = blocks[start+k]
                    blocks[start+k] = -1
                break

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] != -1:
            checksum += i*blocks[i]

    print(checksum)

if __name__ == "__main__":
    main()