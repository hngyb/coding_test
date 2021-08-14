h, w, x, y = map(int, input().split())

a = [[0 for _ in range(w)] for _ in range(h)]
b = []
for i in range(h+x):
    b.append(list(map(int, input().split())))

for i in range(h):
    for j in range(w):
        a[i][j] = b[i][j]

for i in range(h):
    for j in range(w):
        if i-x >= 0 and j-y >= 0:
            a[i][j] = a[i][j] - a[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()
