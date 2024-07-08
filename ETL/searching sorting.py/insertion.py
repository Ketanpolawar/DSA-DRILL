arr = [1, 7, 2, 3, 9, 4, 5, 6]

for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        j -= 1

print(arr)
