#-*- coding:utf-8 -*-

# 카드 정렬하기 (boj 1715)
# heapq 사용, 새로 합친 카드 묶음도 추가

import heapq

def solution():
    n = int(input())
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(input()))
    
    result = 0
    while len(heap) != 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)

        sum = first + second
        result += sum
        heapq.heappush(heap, sum)
    
    print(result)

solution()