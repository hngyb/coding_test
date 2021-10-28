#-*- coding:utf-8 -*-

# 국영수 (boj 10825)
# sort 함수 key 활용

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        student = input().split()
        arr.append((student[0], student[1], student[2], student[3]))
    
    arr.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    for student in arr:
        print(student[0])

solution()