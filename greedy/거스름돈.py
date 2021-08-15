# 거스름돈
# boj 5585번

def solution():
    pay = int(input())
    change = 1000 - pay
    count = 0

    coin_types = [500, 100, 50, 10, 5, 1]

    for coin in coin_types:
        count += change // coin
        change = change % coin
    
    print(count)

solution()