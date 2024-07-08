#roatating the matrix by 90 take the traspose and reeverse the rows
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Step 1: Transpose the matrix
for i in range(len(a)):
    for j in range(i + 1, len(a[0])):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp
# Step 2: Reverse each row
for i in a:
    k = 0
    m = len(i) - 1
    for p in range(m//2):
        temp = i[k]
        i[k] = i[m]
        i[m] = temp
        k += 1
        m -= 1
print("After reversing each row:")
for row in a:
    print(row)
