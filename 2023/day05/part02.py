# Advent of Code 2023
#
# Day 5: If You Give A Seed A Fertilizer (Part Two)
#
# The almanac starts by listing which seeds need to be planted. The values on the
# initial seeds line come in pairs. Within each pair, the first value is the
# start of the range and the second value is the length of the range.
#
# The rest of the almanac contains a list of maps which describe how to convert
# numbers from a source category into numbers in a destination category. Each
# line within a map contains three numbers: the destination range start, the
# source range start, and the range length. Any source numbers that aren't mapped
# correspond to the same destination number. Provide the lowest location number
# that corresponds to any of the initial seed numbers.
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
# - Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# - Seed 82, soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, location 46.
# The lowest location number in this example is 46.


def parse_seeds(line):
    result = []
    seeds = line.split(": ")[1].rstrip().split(" ")

    for i in range(0, len(seeds), 2):
        start = int(seeds[i])
        end = start + int(seeds[i + 1]) - 1
        result.append([start, end])

    return sorted(result)


def parse_almanac(lines):
    seeds = parse_seeds(lines[0])

    maps = []
    ranges = []

    i = 3
    while i < len(lines):
        if lines[i] == "\n":
            maps.append(sorted(ranges))
            ranges = []
            i += 2
        else:
            r = lines[i].rstrip().split(" ")
            r = list(map(int, r))
            ranges.append(r)
            i += 1
    maps.append(sorted(ranges))

    return seeds, maps


def rev_map(value, maps):
    for map in reversed(maps):
        for dststart, srcstart, rnglen in map:
            if dststart <= value and value < dststart + rnglen:
                value = srcstart + (value - dststart)
                break

    return value


def location_search_range(seeds, maps):
    ranges = maps[-1]
    start = 0
    i = 0

    while i < len(ranges):
        end = ranges[i][0] - 1

        if start == ranges[i][0]:
            end = start + ranges[i][2] - 1
            i += 1

        low, high = sorted([rev_map(start, maps), rev_map(end, maps)])

        for s in seeds:
            if low <= s[1] and high >= s[0]:
                return start, end

        start = end + 1


def num_in_seeds(num, seeds):
    for s in seeds:
        if num >= s[0] and num <= s[1]:
            return True

    return False


def find_lowest_location(s, e, seeds, maps):
    lowest = e

    while s <= e:
        mid = s + (e - s) // 2

        if num_in_seeds(rev_map(mid, maps), seeds):
            lowest = min(lowest, mid)
            e = mid - 1
        else:
            s = mid + 1

    return lowest


def lowest_location_num(almanac):
    lines = None
    with open(almanac) as f:
        lines = f.readlines()

    seeds, maps = parse_almanac(lines)
    start, end = location_search_range(seeds, maps)
    return find_lowest_location(start, end, seeds, maps)


test_result = lowest_location_num("test_input")
print(f"test input result: {test_result}")

puzzle_result = lowest_location_num("puzzle_input")
print(f"puzzle input result: {puzzle_result}")
