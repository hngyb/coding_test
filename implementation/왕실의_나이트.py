# 왕실의 나이트
# idea: 시뮬레이션 문제: 상하좌우 * 2(경우의 수) = 8가지
# letter to number: ord(col) - 96
def solution():
    start = input()
    row =  int(start[1])
    col = ord(start[0]) - 96

    # (row,col)
    move_types = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, -2), (-1, -2), (1, 2), (-1, 2)]
    
    count = 0
    for m in move_types:
        moved_row = row + m[0]
        moved_col = col + m[1]
        if moved_row >= 1 and moved_row <= 8 and moved_col >= 1 and moved_col <= 8:
            count += 1
    print(count)

solution()