# Advent of Code 2023
#
# Day 4: Scratchcards
#
# Total points of scrtchards. Each card has two lists of numbers separated by a
# vertical bar (|): a list of winning numbers and a list of numbers you have.
# The first match is worth one point and each match after the first doubles the
# point value of the card.
#
# Test input:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
#
# Test answer:
# - Card 1 has five winning numbers (41, 48, 83, 86, and 17): 8 points
# - Card 2 has two winning numbers (32 and 61): 2 points
# - Card 3 has two winning numbers (1 and 21): 2 points
# - Card 4 has one winning number (84): 1 point
# - 13 total points


def scratchcard_points(table):
    total = 0

    cards = None
    with open(table) as f:
        cards = f.readlines()

    for card in cards:
        _, winning = card.rstrip().split(": ")
        winning, tocheck = winning.split(" | ")
        winning = winning.split(" ")
        tocheck = tocheck.split(" ")
        points = 0

        for num in tocheck:
            if num != "" and num in winning:
                if points < 1:
                    points = 1
                else:
                    points *= 2

        total += points

    return total


test_result = scratchcard_points("test_input")
print(f"test input result: {test_result}")

puzzle_result = scratchcard_points("puzzle_input")
print(f"puzzle input result: {puzzle_result}")
