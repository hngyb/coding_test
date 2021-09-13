# 이것이 코딩 테스트다: 음료수 얼려 먹기
# idea: graph 자체에 visit과 같이 처리

import sys
from collections import deque

def BFS_solution():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip()))) # str은 iterable, map을 적용하면 문자(char) 단위로 돌면서 적용이 되어 리스트 형식으로 쪼개질 수 있음.
    queue = deque([])
    # 상하좌우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                continue
            queue.append((i, j))
            graph[i][j] = 1
            
            while queue:
                (x, y) = queue.popleft()
                for d in range(4):
                    moved_x = x + dx[d]
                    moved_y = y + dy[d]
                    if moved_x >= n or moved_x < 0 or moved_y >= m or moved_y < 0:
                        continue
                    if graph[moved_x][moved_y] == 0:
                        queue.append((moved_x, moved_y))
                        graph[moved_x][moved_y] = 1
            print()
            answer += 1
    
    print(answer)
    return answer

BFS_solution()