# multiple types of sorting
num = [1, 23, 2, 3, 5, 6, 8, 94, 56, 435]

n = len(num)

for i in range(n):
    minIndex = i

    for j in range(i + 1, n):
        if num[j] < num[minIndex]:
            minIndex = j

    # swap values using index
    num[i], num[minIndex] = num[minIndex], num[i]

print(num)




