def check(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return True
    return False

def pageFaults(N, C, pages):
    arr = []
    count = 0
    for i in range(N):
        if len(arr) < C:
            if not check(arr, pages[i]):
                arr.append(pages[i])
                count += 1
            else:
                arr.remove(pages[i])
                arr.append(pages[i])
        else:
            if check(arr, pages[i]):
                arr.remove(pages[i])
                arr.append(pages[i])
            else:
                arr.pop(0)
                arr.append(pages[i])
                count += 1
    return count

# Example usage:
N = 7
C = 4
pages = [1, 2, 1, 3, 4, 5, 1]
print(pageFaults(N, C, pages))  # Output: 5
