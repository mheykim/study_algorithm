T = int(input())
code0 = [0, 0, 0, 1, 1, 0, 1]
code1 = [0, 0, 1, 1, 0, 0, 1]
code2 = [0, 0, 1, 0, 0, 1, 1]
code3 = [0, 1, 1, 1, 1, 0, 1]
code4 = [0, 1, 0, 0, 0, 1, 1]
code5 = [0, 1, 1, 0, 0, 0, 1]
code6 = [0, 1, 0, 1, 1, 1, 1]
code7 = [0, 1, 1, 1, 0, 1, 1]
code8 = [0, 1, 1, 0, 1, 1, 1]
code9 = [0, 0, 0, 1, 0, 1, 1]

for i_test in range(1, T+1):
    N, M = map(int, input().split())
    map_1 = [list(map(int, input())) for _ in range(N)]
    ey = -99
    ex = -99
    flg = False
    for j in range(N):
        for i in range(M-1, -1, -1):
            if map_1[j][i] == 1:
                ey = j
                ex = i + 1
                flg = True
                break
        if flg:
            break
    map_2 = []
    for numi in range(8):
        tmp = []
        for ii in range(7):
            tmp.append(map_1[ey][ex-7*(numi+1)+ii])

        if tmp == code0:
            map_2.append(0)
        elif tmp == code1:
            map_2.append(1)
        elif tmp == code2:
            map_2.append(2)
        elif tmp == code3:
            map_2.append(3)
        elif tmp == code4:
            map_2.append(4)
        elif tmp == code5:
            map_2.append(5)
        elif tmp == code6:
            map_2.append(6)
        elif tmp == code7:
            map_2.append(7)
        elif tmp == code8:
            map_2.append(8)
        elif tmp == code9:
            map_2.append(9)

    # val1 = (map_2[0]+map_2[2]+map_2[4]+map_2[6])*3 + (map_2[1]+map_2[3]+map_2[5]+map_2[7])
    val2 = (map_2[0] + map_2[2] + map_2[4] + map_2[6]) + (map_2[1] + map_2[3] + map_2[5] + map_2[7]) * 3
    if val2 % 10 == 0:
        ans = sum(map_2)
    else:
        ans = 0
    print("#{}".format(i_test), end=" ")
    print(ans)
