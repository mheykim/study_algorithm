T = int(input())
def check():
    global map_1, ans

    for j in range(9):
        tmp = []
        for i in range(9):
            if map_1[j][i] in tmp:
                ans = 0
                return
            else:
                tmp.append(map_1[j][i])

    for i in range(9):
        tmp = []
        for j in range(9):
            if map_1[j][i] in tmp:
                ans = 0
                return
            else:
                tmp.append(map_1[j][i])

    for ii in range(3):
        for jj in range(3):
            ey, ex = jj*3, ii*3
            tmp = []
            for i in range(3):
                for j in range(3):
                    if map_1[ey+j][ex+i] in tmp:
                        ans = 0
                        return
                    else:
                        tmp.append(map_1[ey+j][ex+i])
    ans = 1
    return

for test_i in range(1, T+1):
    map_1 = [list(map(int, input().split()))for _ in range(9)]
    ans = -99
    check()
    print("#{}".format(test_i), end=" ")
    print(ans)