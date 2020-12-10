#!/usr/bin/env python3

# Part 1
with open("data.txt") as input_file:
    boardingpasses = input_file.read().splitlines()


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def bin_search(seat_string, seat_range):
    direction = seat_string[0]
    lower_range, upper_range = split_list(seat_range)

    if direction in ("F", "L"):
        new_range = lower_range
    elif direction in ("B", "R"):
        new_range = upper_range
    if len(new_range) == 1:
        return new_range[0]

    return bin_search(seat_string[1:], new_range)


def split_boardingpass(boardingpass):
    return boardingpass[:-3], boardingpass[-3:]


def get_seat_id(row, column):
    return row * 8 + column


def main():
    SEAT_ROWS = 128
    SEAT_COLUMNS = 8
    seat_ids = []
    for boardingpass in boardingpasses:
        row_str, column_str = split_boardingpass(boardingpass)
        row = bin_search(row_str, range(SEAT_ROWS))
        column = bin_search(column_str, range(SEAT_COLUMNS))
        seat_ids.append(get_seat_id(row, column))

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
