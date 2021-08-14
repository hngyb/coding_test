n = int(input())

for i in range(1, n + 1):
    blank = n - 1;
    print(blank * ' ', end = '')
    print(i * '* ')
    n = n - 1