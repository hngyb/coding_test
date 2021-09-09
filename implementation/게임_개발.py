# 게임 개발
# idea: 시뮬레이션 문제
# 방문 체크, 회전 횟수 기록!
# 북쪽이 -1!
# list comprehension: array = [[0] * m for _ in range(n)]

def solution():
    n, m = map(int, input().split())
    x, y, direction = map(int, input().split())
    dx = [-1, 0, 1, 0] # 북, 동, 남, 서
    dy = [0, 1, 0, -1]

    v = [[0] * m for _ in range(n)]
    v[x][y] = 1

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    def turn_left(direction):
        direction -= 1
        if direction == -1: direction = 3
        return direction

    count = 1
    turn_time = 0 # 회전 횟수를 기록하기 위한 변수
    while True:
        direction = turn_left(direction)
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if v[nx][ny] == 0 and arr[nx][ny] == 0: # 가보지 않았고, 육지인 경우
            x = nx
            y = ny
            count += 1
            turn_time = 0
            v[x][y] = 1 # 방문 체크
            continue
        else:
            turn_time += 1
        
        if turn_time == 4: # 네 방향 모두 갈 수 없는 경우
            nx = x - dx[direction]
            ny = y - dy[direction]
            if arr[nx][ny] == 0: 
                x = nx
                y = ny
            else: # 뒤가 바다로 막혀있는 경우
                break
            turn_time = 0
    
    print(count)

solution()


