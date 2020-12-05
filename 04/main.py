#!/usr/bin/env python3

def raw_passport_to_dict(raw_passport):
    passport_line = " ".join(raw_passport.splitlines())
    fields = passport_line.split(" ")
    return dict(field.split(":") for field in fields)


def validate_passport(passport,
                      required_fields=["pid", "ecl", "eyr",
                                       "hcl", "byr", "iyr", "hgt"],
                      optional_fields=["cid"]):
    if all(field in passport.keys() for field in required_fields):
        return True
    return False


def main():
    with open("data.txt", "r") as input:
        raw_passports = input.read().split("\n\n")
    passports = [raw_passport_to_dict(raw_passport)
                 for raw_passport in raw_passports]
    valid_passports = [
        passport for passport in passports if validate_passport(passport)]
    print(len(valid_passports))


if __name__ == "__main__":
    main()
