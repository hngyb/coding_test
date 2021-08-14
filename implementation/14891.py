import sys

'''
a[2] - b[6,2] - c[6,2] - d[6]
a[i*8+2] - b[i*8+6, i*8+2] - c[i*8+6, i*8+2] - d[i*8+6]
시계 방향:
a[8] = a[7], a[9] = a[0], a[10] = a[1], ...
a[16] = a[15], a[17] = a[8], a[18] = a[9], ...
a[24] = a[23], a[25] = a[16], a[26] = a[17], ...
for j in range(8):
    if i*8 + j % 8 == 0:
        a[i*8 + j] = a[i*8 +j - 1]
    else:
        a[i*8 + j] = a[i*8 +j - 9]

반시계 방향:
a[8] = a[1], a[9] = a[2], a[10] = a[3], ... a[15] = a[0]
a[16] = a[9], a[17] = a[10], ..., a[23] = a[8]
for j in range(8):
    if i*8 + j % 8 == 7:
        a[i*8+j] = a[i*8+j-15]
    else:
        a[i*8+j] = a[i*8+j-7]
'''
def solve():
    a = b = c = d = [0] * 800
    a = list(map(int,list(sys.stdin.readline().rstrip()))) + a
    b = list(map(int,list(sys.stdin.readline().rstrip()))) + b
    c = list(map(int,list(sys.stdin.readline().rstrip()))) + c
    d = list(map(int,list(sys.stdin.readline().rstrip()))) + d
    k = int(sys.stdin.readline())
    a_count = b_count = c_count = d_count = 0

    for _ in range(k):
        n, dir = map(int, sys.stdin.readline().split())
        flags = [[0 for _ in range(2)] for _ in range(4)]

        if n == 1: # a 회전
            flags[0][0] = 1
            flags[0][1] = dir
            if a[a_count*8 + 2] != b[b_count*8 + 6]: # b 회전
                flags[1][0] = 1
                flags[1][1] = flags[0][1] * -1
                if b[b_count*8 + 2] != c[c_count*8 + 6]: # c 회전
                    flags[2][0] = 1
                    flags[2][1] = flags[1][1] * -1
                    if c[c_count*8 + 2] != d[d_count*8 + 6]: # d 회전
                        flags[3][0] = 1
                        flags[3][1] = flags[2][1] * -1
            for i, v in enumerate(flags):
                if i == 0: # a
                    if v[0] == 1:
                        a_count = a_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 0:
                                    a[a_count*8+j] = a[a_count*8+j-1]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 7:
                                    a[a_count*8+j] = a[a_count*8+j-15]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-7]
                elif i == 1: # b
                    if v[0] == 1:
                        b_count = b_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 0:
                                    b[b_count*8+j] = b[b_count*8+j-1]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 7:
                                    b[b_count*8+j] = b[b_count*8+j-15]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-7]
                elif i == 2: # c
                    if v[0] == 1:
                        c_count = c_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 0:
                                    c[c_count*8+j] = c[c_count*8+j-1]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 7:
                                    c[c_count*8+j] = c[c_count*8+j-15]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-7]
                elif i == 3: # d
                    if v[0] == 1:
                        d_count = d_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 0:
                                    d[d_count*8+j] = d[d_count*8+j-1]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 7:
                                    d[d_count*8+j] = d[d_count*8+j-15]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-7]
        elif n == 2: # b 회전
            flags[1][0] = 1
            flags[1][1] = dir
            if a[a_count*8 + 2] != b[b_count*8 + 6]: # a 회전
                flags[0][0] = 1
                flags[0][1] = flags[1][1] * -1
            if b[b_count*8 + 2] != c[c_count*8 + 6]: # c 회전
                flags[2][0] = 1
                flags[2][1] = flags[1][1] * -1
                if c[c_count*8 + 2] != d[d_count*8 + 6]: # d 회전
                    flags[3][0] = 1
                    flags[3][1] = flags[2][1] * -1
            for i, v in enumerate(flags):
                if i == 0: # a
                    if v[0] == 1:
                        a_count = a_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 0:
                                    a[a_count*8+j] = a[a_count*8+j-1]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 7:
                                    a[a_count*8+j] = a[a_count*8+j-15]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-7]
                elif i == 1: # b
                    if v[0] == 1:
                        b_count = b_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 0:
                                    b[b_count*8+j] = b[b_count*8+j-1]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 7:
                                    b[b_count*8+j] = b[b_count*8+j-15]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-7]
                elif i == 2: # c
                    if v[0] == 1:
                        c_count = c_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 0:
                                    c[c_count*8+j] = c[c_count*8+j-1]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 7:
                                    c[c_count*8+j] = c[c_count*8+j-15]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-7]
                elif i == 3: # d
                    if v[0] == 1:
                        d_count = d_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 0:
                                    d[d_count*8+j] = d[d_count*8+j-1]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 7:
                                    d[d_count*8+j] = d[d_count*8+j-15]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-7]
        elif n == 3: # c 회전
            flags[2][0] = 1
            flags[2][1] = dir
            if b[b_count*8 + 2] != c[c_count*8 + 6]: # b 회전
                flags[1][0] = 1
                flags[1][1] = flags[2][1] * -1
                if a[a_count*8 + 2] != b[b_count*8 + 6]: # a 회전
                    flags[0][0] = 1
                    flags[0][1] = flags[1][1] * -1
            if c[c_count*8 + 2] != d[d_count*8 + 6]: # d 회전
                flags[3][0] = 1
                flags[3][1] = flags[2][1] * -1
            for i, v in enumerate(flags):
                if i == 0: # a
                    if v[0] == 1:
                        a_count = a_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 0:
                                    a[a_count*8+j] = a[a_count*8+j-1]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 7:
                                    a[a_count*8+j] = a[a_count*8+j-15]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-7]
                elif i == 1:  # b
                    if v[0] == 1:
                        b_count = b_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 0:
                                    b[b_count*8+j] = b[b_count*8+j-1]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 7:
                                    b[b_count*8+j] = b[b_count*8+j-15]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-7]
                elif i == 2: # c
                    if v[0] == 1:
                        c_count = c_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 0:
                                    c[c_count*8+j] = c[c_count*8+j-1]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 7:
                                    c[c_count*8+j] = c[c_count*8+j-15]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-7]
                elif i == 3: # d
                    if v[0] == 1:
                        d_count = d_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 0:
                                    d[d_count*8+j] = d[d_count*8+j-1]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 7:
                                    d[d_count*8+j] = d[d_count*8+j-15]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-7]
        elif n == 4: # d 회전
            flags[3][0] = 1
            flags[3][1] = dir
            if c[c_count*8 + 2] != d[d_count*8 + 6]: # c 회전
                flags[2][0] = 1
                flags[2][1] = flags[3][1] * -1
                if b[b_count*8 + 2] != c[c_count*8 + 6]: # b 회전
                    flags[1][0] = 1
                    flags[1][1] = flags[2][1] * -1
                    if a[a_count*8 + 2] != b[b_count*8 + 6]: # a 회전
                        flags[0][0] = 1
                        flags[0][1] = flags[1][1] * -1
            for i, v in enumerate(flags):
                if i == 0:  # a
                    if v[0] == 1:
                        a_count = a_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 0:
                                    a[a_count*8+j] = a[a_count*8+j-1]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (a_count*8+j) % 8 == 7:
                                    a[a_count*8+j] = a[a_count*8+j-15]
                                else:
                                    a[a_count*8+j] = a[a_count*8+j-7]
                elif i == 1: # b
                    if v[0] == 1:
                        b_count = b_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 0:
                                    b[b_count*8+j] = b[b_count*8+j-1]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (b_count*8+j) % 8 == 7:
                                    b[b_count*8+j] = b[b_count*8+j-15]
                                else:
                                    b[b_count*8+j] = b[b_count*8+j-7]
                elif i == 2: # c
                    if v[0] == 1:
                        c_count = c_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 0:
                                    c[c_count*8+j] = c[c_count*8+j-1]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (c_count*8+j) % 8 == 7:
                                    c[c_count*8+j] = c[c_count*8+j-15]
                                else:
                                    c[c_count*8+j] = c[c_count*8+j-7]
                elif i == 3: # d
                    if v[0] == 1:
                        d_count = d_count + 1
                        if v[1] == 1: # 시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 0:
                                    d[d_count*8+j] = d[d_count*8+j-1]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-9]
                        elif v[1] == -1: # 반시계 방향
                            for j in range(8):
                                if (d_count*8+j) % 8 == 7:
                                    d[d_count*8+j] = d[d_count*8+j-15]
                                else:
                                    d[d_count*8+j] = d[d_count*8+j-7]
    
    ans = 0
    ans = ans + 1 if a[a_count * 8] == 1 else ans
    ans = ans + 2 if b[b_count * 8] == 1 else ans
    ans = ans + 4 if c[c_count * 8] == 1 else ans
    ans = ans + 8 if d[d_count * 8] == 1 else ans
    print(ans)

solve()