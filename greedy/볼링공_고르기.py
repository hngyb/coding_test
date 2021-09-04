# 볼링공 고르기
# idea:
# 볼링공을 하나씩 보면서 뒤에 있는 볼링공과 무게가 다르면 경우의 수 + 1 (x) -> cost high
# 조합 구하고, 같은 무게를 가진 볼링공의 경우의 수 빼기 (o)

import sys

def my_solution():
    n, m = map(int, input().split())
    k = list(map(int, sys.stdin.readline().split()))

    # 조합 구하기
    result = n * (n - 1) / 2

    # 무게가 같은 경우 세기
    a = n - len(set(k))
    result -= a
    
    print(int(result))

my_solution()