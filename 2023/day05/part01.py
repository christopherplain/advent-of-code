# Advent of Code 2023
#
# Day 5: If You Give A Seed A Fertilizer
#
# The almanac starts by listing which seeds need to be planted. The rest of the
# almanac contains a list of maps which describe how to convert numbers from a
# source category into numbers in a destination category. Each line within a map
# contains three numbers: the destination range start, the source range start,
# and the range length. Any source numbers that aren't mapped correspond to the
# same destination number. Provide the lowest location number that corresponds
# to any of the initial seed numbers.
#
# Test input:
# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4
#
# Test answer:
# - Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# - Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# - Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# - Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
# The lowest location number in this example is 35.


def parse_almanac(lines):
    seeds = lines[0].split(": ")[1].rstrip().split(" ")
    seeds = list(map(int, seeds))

    maps = []
    ranges = []

    i = 3
    while i < len(lines):
        if lines[i] == "\n":
            maps.append(ranges)
            ranges = []
            i += 2
        else:
            r = lines[i].rstrip().split(" ")
            r = list(map(int, r))
            ranges.append(r)
            i += 1
    maps.append(ranges)

    return seeds, maps


def map_values(values, map):
    for i, value in enumerate(values):
        for r in map:
            if r[1] <= value and value <= r[1] + r[2] - 1:
                values[i] = value - r[1] + r[0]
                break

    return values


def lowest_location_num(almanac):
    lines = None
    with open(almanac) as f:
        lines = f.readlines()

    mapped_values, maps = parse_almanac(lines)

    for map in maps:
        mapped_values = map_values(mapped_values, map)

    lowest_value = float("inf")
    for value in mapped_values:
        lowest_value = min(lowest_value, value)

    return lowest_value


test_result = lowest_location_num("test_input")
print(f"test input result: {test_result}")

puzzle_result = lowest_location_num("puzzle_input")
print(f"puzzle input result: {puzzle_result}")
