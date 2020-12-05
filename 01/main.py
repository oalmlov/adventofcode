#!/usr/bin/env python3
from itertools import combinations
from math import prod

with open("data.txt", "r") as input_file:
    input_lines = input_file.readlines()


def find_combo(data, n_combinations, value):
    for combo in combinations(data, n_combinations):
        if sum(combo) == value:
            return prod(combo)


input = [int(n) for n in input_lines]

# Part 1
print(find_combo(input, 2, 2020))

# Part 2
print(find_combo(input, 3, 2020))
