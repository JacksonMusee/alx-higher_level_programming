#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0

    if isinstance(roman_string, str) is False or roman_string is None:
        return num

    for i, v in enumerate(roman_string):
        if i < (len(roman_string) - 1) and rom_int[roman_string[i]] <\
                rom_int[roman_string[i + 1]]:
            num = num - rom_int[roman_string[i]]
        else:
            num = num + rom_int[roman_string[i]]
    return num
