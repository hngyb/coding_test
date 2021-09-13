# 이것이 코딩 테스트다: 미로 탈출
# idea: graph의 값을 움직인 횟수로 update (+1)

import sys
from collections import deque

def solution():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip())))
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0,0)])
    while queue:
        (x, y) = queue.popleft()
        for d in range(4):
            moved_x = x + dx[d]
            moved_y = y + dy[d]
            if moved_x < 0 or moved_x >= n or moved_y < 0 or moved_y >= m:
                continue
            if graph[moved_x][moved_y] == 1:
                graph[moved_x][moved_y] = graph[x][y] + 1
                queue.append((moved_x, moved_y))

    return graph[n-1][m-1]

print(solution())
