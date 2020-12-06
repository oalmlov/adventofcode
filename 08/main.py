#!/usr/bin/env python3
from copy import deepcopy

with open("data.txt", "r") as input_file:
    instruction_strings = input_file.readlines()


def parse_instruction(instruction_string):
    split_instruction = instruction_string.split()
    return (split_instruction[0], int(split_instruction[1]))


def exec_instruction(state, action, value):
    working_state = deepcopy(state)
    working_state["visited_indexes"].append(working_state["current_index"])
    if action == "jmp":
        working_state["current_index"] += value
    elif action == "acc":
        working_state["accumulator"] += value
        working_state["current_index"] += 1
    elif action == "nop":
        working_state["current_index"] += 1
    return working_state


def run_instructions(state):
    if state["current_index"] in state["visited_indexes"]:
        return state
    action, value = state["instructions"][state["current_index"]]
    new_state = exec_instruction(state, action, value)
    return run_instructions(new_state)


def main():
    instructions = [parse_instruction(instruction_string)
                    for instruction_string in instruction_strings]
    state = {"current_index": 0, "visited_indexes": [],
             "accumulator": 0, "instructions": instructions}
    new_state = run_instructions(state)
    print(new_state["accumulator"])


if __name__ == "__main__":
    main()
