marks = [int(input(f"Enter test {i + 1} marks ")) for i in range(3)]
print(f"Average of best two: {(sum(marks) - min(marks)) // 2}")