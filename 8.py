class PaliStr:
    @staticmethod
    def is_palindrome(input_str):
        return input_str == input_str[::-1]

class PaliInt(PaliStr):
    @staticmethod
    def is_palindrome(val):
        return str(val) == str(val)[::-1]

input_str = input("Enter a string: ")
if PaliStr.is_palindrome(input_str):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")

input_val = int(input("Enter an integer: "))
if PaliInt.is_palindrome(input_val):
    print("Given integer is a palindrome")
else:
    print("Given integer is not a palindrome")
