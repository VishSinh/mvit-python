def roman_to_dec(rom_str):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for i in range(len(rom_str) - 1, -1, -1):
        left_val = roman_dict[rom_str[i]]
        value += left_val if left_val >= value else -left_val
    return value
roman_str = input("Enter a Roman Number: ")
print(roman_to_dec(roman_str))
