import re

def is_phone_number(phone_num):
    return len(phone_num) == 12 and all(ch.isdigit() if i != 3 and i != 7 else ch == '-' for i, ch in enumerate(phone_num))

def is_phone_number_regex(phone_num):
    return re.compile(r'^\d{3}-\d{3}-\d{4}$').match(phone_num)

phone_num = input("Enter a phone number: ")
print('Without using RegEx:')
print("Valid Phone Number" if is_phone_number(phone_num) else "Invalid Phone Number")

print('Using RegEx:')
print("Valid Phone Number" if is_phone_number_regex(phone_num) else "Invalid Phone Number")

