# Advent of Code 2023

# Day 2: Cube Conundrum
# Sum of game IDs that are possible if the bag contains only 12 red cubes,
# 13 green cubes, and 14 blue cubes.

# Test input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
#
# Test answer:
# 1 + 2 + 5 = 8


def parse_game(game):
    game_result = {"red": 0, "green": 0, "blue": 0}
    id, counts = game.split(": ")
    id = int(id.split(" ")[1])
    counts = counts.replace(";", ",").split(", ")

    for count in counts:
        num, color = count.split(" ")
        color = color.rstrip()
        game_result[color] = max(game_result[color], int(num))

    return id, game_result


def sum_possible_game_ids(game_record):
    max_cubes = {"red": 12, "green": 13, "blue": 14}
    sum = 0

    with open(game_record) as f:
        games = f.readlines()

        for game in games:
            id, game_result = parse_game(game)

            for color, num in game_result.items():
                if num > max_cubes[color]:
                    id = 0
                    break

            sum += id

    return sum


test_result = sum_possible_game_ids("test_input")
print(f"Sum of test input possible game IDs: {test_result}")

puzzle_result = sum_possible_game_ids("puzzle_input")
print(f"Sum of puzzle input possible game IDs: {puzzle_result}")
