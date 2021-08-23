# 만들 수 없는 금액 (꼭 복습하기!)
# idea: target 이하의 값은 모두 만들 수 있다.

# (예시) 동전의 개수 N=4, 화폐 단위가 1, 2, 3, 8인 경우
# (0) 처음에는 금액 1을 만들 수 있는지 확인하기 위해 target=1로 설정 
# (1) target=1을 만족할 수 있는지 확인 → 만들 수 있으므로 target=2 (1+1)로 업데이트 
# (1까지의 모든 금액을 만들 수 있다는 말과 같음)
# (2) target=2를 만족할 수 있는지 확인 → 화폐 단위가 2인 동전이 있으므로 target=4 (2+2)로 업데이트
# (3까지의 모든 금액을 만들 수 있다는 말과 같음)
# (3) target=4를 만족할 수 있는지 확인 → 화폐 단위가 3인 동전이 있으므로 target=7 (4+3)로 업데이트
# (6까지의 모든 금액을 만들 수 있다는 말과 같음)
# (4) target=7을 만족할 수 있는지 확인 → 7보다 큰 화폐 단위가 8인 동전이 있음
# 따라서 금액 7을 만드는 방법은 없음 (정답은 7)

import sys

def my_solution():
    n = int(input())
    coins = list(map(int, sys.stdin.readline().split()))
    coins.sort()

    target = 1
    for coin in coins:
        if target < coin:
            break
        target = target + coin
    print(target)

my_solution()