# Advent of Code 2023
#
# Day 4: Scratchcards (Part Two)
#
# Win copies of the scratchcards below the winning card equal to the number of
# matches. If card 10 were to have 5 matching numbers, win one copy each of cards
# 11, 12, 13, 14, and 15. Sum number of cards.
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
# 1 instance of card 1, 2 instances of card 2, 4 instances of card 3, 8 instances
# of card 4, 14 instances of card 5, and 1 instance of card 6: 30 cards total


def scratchcard_points(table):
    total = 0

    cards = None
    with open(table) as f:
        cards = f.readlines()

    card_count = [1] * (len(cards))

    for i, card in enumerate(cards):
        _, winning = card.rstrip().split(": ")
        winning, tomatch = winning.split(" | ")
        winning = winning.split(" ")
        tomatch = tomatch.split(" ")

        next_card = i + 1
        for num in tomatch:
            if next_card >= len(card_count):
                break

            if num != "" and num in winning:
                card_count[next_card] += card_count[i]
                next_card += 1

        total += card_count[i]

    return total


test_result = scratchcard_points("test_input")
print(f"test input result: {test_result}")

puzzle_result = scratchcard_points("puzzle_input")
print(f"puzzle input result: {puzzle_result}")
