# Advent of Code 2023

# Day 2: Cube Conundrum (Part Two)
# Find the minimum set of cubes that must have been present for each game, and
# sum the power of these sets.

# Test input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#
# Test answer:
# 48 + 12 + 1560 + 630 + 36 = 2286


def parse_game(game):
    game_result = {"red": 0, "green": 0, "blue": 0}
    counts = game.split(": ")[1].replace(";", ",").split(", ")

    for count in counts:
        num, color = count.split(" ")
        color = color.rstrip()
        game_result[color] = max(game_result[color], int(num))

    return game_result


def sum_possible_game_ids(game_record):
    sum = 0

    with open(game_record) as f:
        games = f.readlines()

        for game in games:
            game_result = parse_game(game)
            product = 1

            for num in game_result.values():
                product *= num

            sum += product

    return sum


test_result = sum_possible_game_ids("test_input")
print(f"Sum of test input possible game IDs: {test_result}")

puzzle_result = sum_possible_game_ids("puzzle_input")
print(f"Sum of puzzle input possible game IDs: {puzzle_result}")
