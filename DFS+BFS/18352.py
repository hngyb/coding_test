# 특정 거리의 도시 찾기 (boj 18352번)
# pypy3로 제출해야 시간초과 안 뜸

from collections import deque

def solution():
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        
    visited = [False] * (n+1)
    queue = deque([(x, 0)])
    visited[x] = True
    
    result = []
    while queue:
        v = queue.popleft()
        count = v[1] + 1
        for i in graph[v[0]]:
            if not visited[i]:
                queue.append((i, count))
                visited[i] = True
                if count == k:
                    result.append(i)
    
    if len(result) == 0:
        print(-1)
    
    else :
        result.sort()
        for i in result:
            print(i)

solution()