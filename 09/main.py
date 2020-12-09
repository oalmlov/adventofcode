#!/usr/bin/env python3
from itertools import combinations

with open("data.txt", "r") as input_file:
    input = input_file.readlines()

# Part 1
def get_sums(data):
    return [sum(combination) for combination in combinations(data, 2)]


def find_invalid_number(data, step=25):
    current_value = data[step]
    if current_value not in get_sums(data[:step]):
        return current_value
    return find_invalid_number(data[1:], step=step)


xmas_data = [int(i) for i in input]
invalid_number = (find_invalid_number(xmas_data, step=25))
print(invalid_number)
