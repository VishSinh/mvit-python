def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current

arr = [int(i) for i in input("Enter a list of numbers: ").split()]
insertion_sort(arr)
print("Sorted array is:")
print(*arr)
