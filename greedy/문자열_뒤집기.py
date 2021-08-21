# 문자열 뒤집기
# idea: 0 묶음, 1 묶음 개수 비교해서 적은 거 선택해서 뒤집기

import sys

def my_solution():
    s = sys.stdin.readline().rstrip()
    zero_num = 0 # 0 묶음 개수
    one_num = 0 # 1 묶음 개수
    before = s[0] # 연속되는 숫자 비교를 위한 변수

    for n in s:
        if before == n: continue # 연속된 숫자
        else: # 연속된 숫자가 달라지는 경우
            if before == '0':
                zero_num = zero_num + 1
            else:
                one_num = one_num + 1
        before = n

    # 마지막 묶음 개수 추가
    if s[-1] == '0': zero_num = zero_num + 1
    else: one_num = one_num + 1

    result = min(zero_num, one_num)
    print(result)

my_solution()