# 곱하기 혹은 더하기
# idea: 둘 중 하나가 0인 경우만 더하는 걸로 생각했으나, 1일 때도 더해줘야 함.
# 둘 중 하나가 1 이하인 경우 더해주기

import sys
def my_solution():
    s = sys.stdin.readline().rstrip()
    
    result = 0
    for n in s:
        a = int(n)
        result = result + a if result <= 1 or a <= 1 else result * a
    print(result)

my_solution()