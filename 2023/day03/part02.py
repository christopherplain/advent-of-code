# Advent of Code 2023
#
# Day 3: Gear Ratios (Part Two)
#
# Sum gear ratios in engine schematic. A gear is any "*" symbol that is adjacent
# to exactly two part numbers. Its gear ratio is the result of multiplying those
# two numbers together.
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
# (467 * 35) + (755 * 598) = 467835


def isasterisk(char):
    return char == "*"


def sum_part_numbers(schematic):
    sum = 0

    lines = None
    with open(schematic) as f:
        lines = f.readlines()

    possible_gears = {}

    for l, line in enumerate(lines):
        line = line.rstrip()
        prev_line = lines[l - 1] if l > 0 else "." * len(line)
        next_line = lines[l + 1] if l < len(lines) - 1 else "." * len(line)
        prev_line = prev_line.rstrip()
        next_line = next_line.rstrip()

        num = ""
        asterisks = []

        for c, char in enumerate(line):
            if char.isdigit():
                num += char
                if isasterisk(prev_line[c]):
                    asterisks.append((l - 1, c))
                if isasterisk(next_line[c]):
                    asterisks.append((l + 1, c))

                if c > 0:
                    if isasterisk(prev_line[c - 1]):
                        asterisks.append((l - 1, c - 1))
                    if isasterisk(line[c - 1]):
                        asterisks.append((l, c - 1))
                    if isasterisk(next_line[c - 1]):
                        asterisks.append((l + 1, c - 1))

                if c < len(line) - 1:
                    if isasterisk(prev_line[c + 1]):
                        asterisks.append((l - 1, c + 1))
                    if isasterisk(line[c + 1]):
                        asterisks.append((l, c + 1))
                    if isasterisk(next_line[c + 1]):
                        asterisks.append((l + 1, c + 1))

            if not char.isdigit() or c == len(line) - 1:
                for al, ac in asterisks:
                    if al in possible_gears and ac in possible_gears[al]:
                        sum += possible_gears[al][ac] * int(num)
                        break

                while asterisks:
                    al, ac = asterisks.pop()
                    if al not in possible_gears:
                        possible_gears[al] = {}
                    possible_gears[al][ac] = int(num)

                num = ""

    return sum


test_result = sum_part_numbers("test_input")
print(f"Sum of test input part numbers: {test_result}")

puzzle_result = sum_part_numbers("puzzle_input")
print(f"Sum of puzzle input part numbers: {puzzle_result}")
