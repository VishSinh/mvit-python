def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)

num_of_terms = int(input("Enter a positive integer: "))
if num_of_terms <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Sequence:")
    print(*[fib(i) for i in range(num_of_terms)])