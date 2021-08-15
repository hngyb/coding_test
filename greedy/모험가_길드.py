# 모험가 길드

# idea: 공포도가 가장 작은 사람부터 그룹핑
def my_code():
    import sys
    from collections import deque

    n = int(input())
    m = list(map(int, sys.stdin.readline().split()))

    m.sort() # 공포도 오름차순 정렬
    m = deque(m)

    result = 0

    while len(m) != 0:
        min_value = m[0]
        m.popleft()

        current_count = 1
        needed_count = min_value - current_count
        while needed_count != 0:
            if len(m) == 0: break
            needed_count = max(needed_count, m[0] - current_count)
            m.popleft()
            current_count += 1
            needed_count = needed_count - 1
        if needed_count == 0: result += 1

    print(result)

# idea: 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같으면, 그룹을 결성할 수 있음
def solution():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in data:
        count += 1
        if count >= i:
            result += 1
            count = 0

    print(result)

# feedback: 
# 공포도 오름차순 정렬까진 괜찮았으나,
# 현재 그룹의 포함된 모험가의 수와 현재 확인하고 있는 공포도를 비교하는 방법에 있어 비효율적임