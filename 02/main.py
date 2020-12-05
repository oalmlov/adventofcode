#!/usr/bin/env python3
from operator import xor

with open("data.txt", "r") as input_file:
    input = input_file.read()

# Part 1
counter = 0
for line in input.splitlines():
    raw_range, raw_char, pattern = line.split()
    n_low = int(raw_range.split("-")[0])
    n_high = int(raw_range.split("-")[1])
    char = raw_char[0]

    allowed_range = range(n_low, n_high + 1)
    char_count = pattern.count(char)

    if char_count in allowed_range:
        counter += 1
print(counter)

# Part 2
counter2 = 0
for line in input.splitlines():
    raw_positions, raw_char, pattern = line.split()
    char = raw_char[:1]
    position1 = int(raw_positions.split("-")[0])
    position2 = int(raw_positions.split("-")[1])

    if xor(pattern[position1 - 1] == char, pattern[position2 - 1] == char):
        counter2 += 1
print(counter2)
