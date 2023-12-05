# Advent of Code 2023
#
# Day 3: Gear Ratios
#
# Sum engine part numbers, which are any numbers adjacent to a symbol, even
# diagonally, not including periods (.).
#
# Test input:
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
#
# Test answer:
# Not part numbers: 114 (top right) and 58 (middle right), sum: 4361


def issymbol(char):
    return not char.isalnum() and char != "."


def sum_part_numbers(schematic):
    sum = 0

    lines = None
    with open(schematic) as f:
        lines = f.readlines()

    for l, line in enumerate(lines):
        line = line.rstrip()
        prev_line = lines[l - 1] if l > 0 else "." * len(line)
        next_line = lines[l + 1] if l < len(lines) - 1 else "." * len(line)
        prev_line = prev_line.rstrip()
        next_line = next_line.rstrip()

        num = ""
        ispart = False

        for c, char in enumerate(line):
            if char.isdigit():
                num += char
                ispart = ispart or issymbol(prev_line[c]) or issymbol(next_line[c])

                if c > 0:
                    ispart = (
                        ispart
                        or issymbol(prev_line[c - 1])
                        or issymbol(line[c - 1])
                        or issymbol(next_line[c - 1])
                    )

                if c < len(line) - 1:
                    ispart = (
                        ispart
                        or issymbol(prev_line[c + 1])
                        or issymbol(line[c + 1])
                        or issymbol(next_line[c + 1])
                    )

            if not char.isdigit() or c == len(line) - 1:
                if ispart:
                    sum += int(num)
                num = ""
                ispart = False

    return sum


test_result = sum_part_numbers("test_input")
print(f"Sum of test input part numbers: {test_result}")

puzzle_result = sum_part_numbers("puzzle_input")
print(f"Sum of puzzle input part numbers: {puzzle_result}")
