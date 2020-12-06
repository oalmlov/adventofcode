#!/usr/bin/env python3

with open("data.txt", "r") as input_file:
    input = input_file.read()
raw_groups_answers = input.split("\n\n")

# Part 1
def get_answers(raw_group_answers):
    yes_answers = []
    members_answers = raw_group_answers.splitlines()
    for member_answer in members_answers:
        for answer in member_answer:
            yes_answers.append(answer)
    # Return a set of unique answers
    return set(yes_answers)


yes_answers = [get_answers(raw_group) for raw_group in raw_groups_answers]
total_yes_answers = sum([len(group_answers) for group_answers in yes_answers])
print(f"Total: {total_yes_answers}")

# Part 2
def get_answers(raw_group_answers):
    yes_answers = []
    members_answers = raw_group_answers.splitlines()
    for member_answer in members_answers:
        for answer in member_answer:
            # If answer exists in all group members answers
            if all([answer in member_answer for member_answer in members_answers]):
                yes_answers.append(answer)
    # Return a set of unique answers
    return set(yes_answers)


groups_yes_answers = [get_answers(raw_group)
                      for raw_group in raw_groups_answers]
total_groups_yes_answers = sum([len(group_answers)
                                for group_answers in groups_yes_answers])
print(f"Total of questions all members answered yes to: {total_groups_yes_answers}")
