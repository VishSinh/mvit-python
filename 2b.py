def binary_to_decimal(binary_num):
    return sum(int(digit) * 2**i for i, digit in enumerate(binary_num[::-1]))
    
def octal_to_hexadecimal(octal_num):
    decimal = sum(int(digit) * 8**i for i, digit in enumerate(octal_num[::-1]))
    hexadecimal = ""
    while decimal != 0:
        remainder = decimal % 16
        hexadecimal = str(remainder) + hexadecimal if remainder <= 9 else chr(ord("A") + (remainder - 10)) + hexadecimal
        decimal //= 16
    return hexadecimal

num = input("Enter a binary number: ")
print(binary_to_decimal(num))

num = input("Enter an octal number: ")
print(octal_to_hexadecimal(num))