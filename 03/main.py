#!/usr/bin/env python3
from math import prod

with open("data.txt", "r") as input_file:
    input = input_file.read()

arrays = input.splitlines()

# Part 1
path = list()
x = 0
for y in range(len(arrays)):
    if x >= len(arrays[y]):
        x = x - len(arrays[y])
    path.append(arrays[y][x])
    x += 3
print(path.count("#"))

# Part 2


def path_finder(arrays, x_step, y_step, start=(0, 0)):
    path = list()
    (x, y) = start

    while y < len(arrays):
        if x >= len(arrays[y]):
            x = x - len(arrays[y])
        path.append((x, y))
        x += x_step
        y += y_step
    return path


paths = [
    path_finder(arrays, 1, 1),
    path_finder(arrays, 3, 1),
    path_finder(arrays, 5, 1),
    path_finder(arrays, 7, 1),
    path_finder(arrays, 1, 2)
]
trees_per_path = list()
for path in paths:
    trees = 0
    for x, y in path:
        if arrays[y][x] == "#":
            trees += 1
    trees_per_path.append(trees)
print(prod(trees_per_path))
