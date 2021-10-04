# 연구소 (boj 14502번)

from collections import deque
from itertools import combinations
from copy import deepcopy

def solution():
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    
    blank = []
    virus = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                blank.append((i, j))
            if graph[i][j] == 2:
                virus.append((i, j))
    wall_case = list(combinations(blank, 3))

    nx = [1, -1, 0, 0]
    ny = [0, 0, -1, 1]
    max_safe_area = 0
    for c in wall_case:
        temp = deepcopy(graph)
        wall1, wall2, wall3 = c
        temp[wall1[0]][wall1[1]] = 1
        temp[wall2[0]][wall2[1]] = 1
        temp[wall3[0]][wall3[1]] = 1
        
        queue = deque(virus)
        visited = virus.copy()
        while queue:
            v = queue.popleft()
            neighbors = []
            for i in range(4):
                neighbors.append((v[0] + nx[i], v[1] + ny[i]))
            for next_node in neighbors:
                if next_node[0] >= 0 and next_node[0] < n and next_node[1] >= 0 and next_node[1] < m:
                    if temp[next_node[0]][next_node[1]] == 0:
                        if not next_node in visited:
                            queue.append(next_node)
                            visited.append(next_node)
                            temp[next_node[0]][next_node[1]] = 2
            
        blank = []
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    blank.append((i, j))
        num_safe_area = len(blank)
        if num_safe_area > max_safe_area:
            max_safe_area = num_safe_area
    
    print(max_safe_area)

solution()