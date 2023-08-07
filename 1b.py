num = input("Enter a value: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")
print('\n'.join([f"{i} appears {num.count(str(i))} times" for i in range(10) if num.count(str(i)) > 0]))