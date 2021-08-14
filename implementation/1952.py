import sys

m, n = map(int, sys.stdin.readline().split())

x = m
y = n

count = 0
while x > 0 and y > 0:
    if x > 2 and y > 2:
        count = count + 4
        x = x - 2
        y = y - 2
    elif x == 2 and y > 1:
        count = count + 2
        x = x - 2
        y = y - 2
    elif y == 2 and x > 2:
        count = count + 3
        x = x - 2
        y = y - 2
    elif x == 1:
        x = x - 1
    elif y == 1 and x > 1:
        count = count + 1
        x = x - 2
        y = y - 1
    elif y == 1 and x == 1:
        x = x - 1
        y = y - 1

print(count)
