#!/usr/bin/env python3

# Part 1
with open("data.txt") as input_file:
    input = input_file.read()


def split_list(the_list):
    half = len(the_list)//2
    return the_list[:half], the_list[half:]


def bin_search(seat_string, index, seat_range):
    current_direction = seat_string[index]
    lower_range, upper_range = split_list(seat_range)

    if current_direction in ["F", "L"]:
        new_range = lower_range
    elif current_direction in ["B", "R"]:
        new_range = upper_range

    if len(new_range) == 1:
        return new_range[0]

    index += 1
    return bin_search(seat_string, index, new_range)


def main():
    seat_ids = []
    boardingpasses = input.splitlines()
    for boardingpass in boardingpasses:
        row_string = boardingpass[:-3]
        column_string = boardingpass[-3:]
        row = bin_search(row_string, 0, range(128))
        column = bin_search(column_string, 0, range(8))
        seat_ids.append((row * 8) + column)

    # Highest seat ID
    print(max(seat_ids))

    # Part 2
    sorted_seat_ids = sorted(seat_ids)
    # Find seat ID missing from the list of seat IDs
    print([x for x in range(sorted_seat_ids[0],
                            sorted_seat_ids[-1])
           if x not in seat_ids])


if __name__ == "__main__":
    main()
