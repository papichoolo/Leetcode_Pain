def sub_sum(top, left, height, width):
    s = 0
    for i in range(top, top + height):
        for j in range(left, left + width):
            s += array[i][j]
    return s

N = int(input())
array = [[0] * 5 for _ in range(5)]

for i in range(N):
    array[i] = list(map(int, input().split()))

S = int(input())
count = 0

for i in range(N):
    for j in range(N):
        size = 1
        _sum = -1

        while i + size <= N and j + size <= N:
            _sum = sub_sum(i, j, size, size)

            if _sum == S:
                count += 1
                break
            elif _sum > S:
                break

            size += 1

print(count)
