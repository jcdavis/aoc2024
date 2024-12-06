import argparse
import re

def main() -> None:
    parser = argparse.ArgumentParser(prog="enqueue_run")
    parser.add_argument("file")
    args = parser.parse_args()
    regex = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
    total = 0
    enabled = True
    with open(args.file) as file:
        for line in file:
            for inst in regex.findall(line):
                if inst[2] == 'do()':
                    enabled = True
                elif inst[3] == "don't()":
                    enabled = False
                elif enabled:
                    total += int(inst[0]) * int(inst[1])

    print(total)

if __name__ == "__main__":
    main()