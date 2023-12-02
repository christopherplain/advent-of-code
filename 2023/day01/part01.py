# Advent of Code 2023

# Day 1: Trebuchet?!
# Combine fist and last digit of each line in doc and sum.

# Test input
# 12, 38, 15, and 77 equals 142
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet


def sum_calibration(doc):
    sum = 0
    with open(doc) as f:
        lines = f.readlines()
        for line in lines:
            digits = "".join(filter(str.isdigit, line))
            num = digits[0] + digits[len(digits) - 1]
            sum += int(num)
    return sum


test_result = sum_calibration("test_input_part01")
print(f"Sum of test input calibration values: {test_result}")

puzzle_result = sum_calibration("puzzle_input")
print(f"Sum of puzzle input calibration values: {puzzle_result}")
