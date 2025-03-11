space = []

for _ in range(100):
    row = [0] * 100
    space.append(row)

n = int(input())


for _ in range(n):
    x, y = map(int, input().split())
    

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            space[i][j] = 1

area = 0

for row in space:
    row_sum = sum(row)
    area += row_sum

print(area)
