# 퍼즐 조각 채우기 (프로그래머스)
from copy import deepcopy
from collections import deque

def bfs(n, type, graph, node, visited):
    nx = [1, -1, 0, 0]
    ny = [0, 0, -1, 1]
    
    ret = [node]
    visited.append(node)
    queue = deque(ret)
    while queue:
        v = queue.popleft()
        
        for i in range(4):
            x = v[0] + nx[i]
            y = v[1] + ny[i]
            if x >= 0 and x < n and y >= 0 and y < n:
                if (x, y) not in visited:
                    visited.append((x,y))
                    if graph[x][y] == type:
                        queue.append((x, y))
                        ret.append((x, y))
    return sorted(ret)

def move_to_zero(block):
    min_x = block[0][0]
    min_y = block[0][1]
    return sorted([(x-min_x, y-min_y) for (x, y) in block])

def block_rotate_90(block, n):
    rotated_block = []
    for (x, y) in block:
        rotated_block.append((y, n-1-x))
    return sorted(rotated_block)

def solution(game_board, table):
    n = len(game_board)
    game_graph = deepcopy(game_board)
    table_graph = deepcopy(table)
    block_list = []
    blank_list = []
    game_visited = []
    table_visited = []
    
    # get block list
    for i in range(n):
        for j in range(n):
            if table_graph[i][j] == 1 and (i,j) not in table_visited:
                block = bfs(n, 1, table_graph, (i, j), table_visited)
                if len(block) > 0:
                    block_list.append(move_to_zero(block))
        
    # get blank list
    for i in range(n):
        for j in range(n):
            if game_graph[i][j] == 0 and (i,j) not in game_visited:
                game_visited.append((i,j))
                blank = bfs(n, 0, game_graph, (i, j), game_visited)
                if len(blank) > 0:
                    blank_list.append(move_to_zero(blank))

    answer = 0
    for block in block_list:
        if block in blank_list:
            answer += len(block)
            blank_list.remove(block)
        else:
            for _ in range(3):
                rotated_block = block_rotate_90(block, n)
                rotated_block = move_to_zero(rotated_block)
                if rotated_block in blank_list:
                    answer += len(rotated_block)
                    blank_list.remove(rotated_block)
                    break
                block = rotated_block
                
    return answer