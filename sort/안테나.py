#-*- coding:utf-8 -*-

# 안테나 (boj 18310)

import sys

def solution():
    n = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    
    middle_point = (n - 1) // 2
    print(arr[middle_point])

solution()