# 성적이 낮은 순서로 학생 출력하기

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        data = input().split()
        arr.append((data[0], data[1]))
    
    arr.sort(key=lambda x:x[1])
    for i in arr:
        print(i[0], end=' ')

solution()