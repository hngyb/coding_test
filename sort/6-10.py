# 위에서 아래로

def solution():
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    nums.sort(reverse=True)
    for i in nums:
        print(i, end=' ')

solution()

