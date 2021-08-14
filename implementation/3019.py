import sys

def solve():
    c, p = map(int, sys.stdin.readline().split())
    f = list(map(int, sys.stdin.readline().split()))
    count = 0

    if p == 1:
        count = c
        for i in range(c):
            if i+3<c:
                if f[i] == f[i+1] and f[i+1] == f[i+2] and f[i+2] == f[i+3]:
                    count = count + 1
    elif p == 2:
        for i in range(c):
            if i+1<c:
                if f[i] == f[i+1]:
                    count = count + 1
    elif p == 3:
        for i in range(c):
            if i+2<c:
                if f[i] == f[i+1] and f[i+2] == f[i+1] + 1:
                    count = count + 1
            if i+1<c:
                if f[i] == f[i+1] + 1:
                    count = count + 1
    elif p == 4:
        for i in range(c):
            if i+2<c:
                if f[i] == f[i+1] + 1 and f[i+1] == f[i+2]:
                    count = count + 1
            if i+1<c:
                if f[i+1] == f[i] + 1:
                    count = count + 1
    elif p == 5:
        for i in range(c):
            if i+2<c:
                if f[i] == f[i+1] and f[i+1] == f[i+2]:
                    count = count + 1
                if f[i] == f[i+2] and f[i] == f[i+1] + 1:
                    count = count + 1
            if i+1<c:
                if f[i+1] == f[i] + 1:
                    count = count + 1
                if f[i] == f[i+1] + 1:
                    count = count + 1
    elif p == 6:
        for i in range(c):
            if i+2<c:
                if f[i] == f[i+1] and f[i+1] == f[i+2]:
                    count = count + 1
                if f[i+1] == f[i+2] and f[i+1] == f[i] + 1:
                    count = count + 1
            if i+1<c:
                if f[i] == f[i+1]:
                    count = count + 1
                if f[i] == f[i+1] + 2:
                    count = count + 1
    elif p == 7:
        for i in range(c):
            if i+2<c:
                if f[i] == f[i+1] and f[i+1] == f[i+2]:
                    count = count + 1
                if f[i] == f[i+1] and f[i+1] == f[i+2] + 1:
                    count = count + 1
            if i+1<c:
                if f[i] == f[i+1]:
                    count = count + 1
                if f[i+1] == f[i] + 2:
                    count = count + 1
    print(count)

solve()