# 무지의 먹방 라이브
# idea: 시간이 적게 걸리는 음식부터 정렬 후 확인 (heapq 사용)
# 다시 풀기!

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_values = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_values + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_values += (now - previous) * length
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_values) % length][1]