T = int(input())
for i_test in range(1, T+1):
    N, M = map(int, input().split())
    map_1 = [list(map(int, input().split())) for _ in range(N)]
    maxv = 0
    for i in range(N-M+1): # 0~3
        for j in range(N-M+1): # 0~3
            tmp = 0
            for ii in range(M): # 0~2
                for jj in range(M): # 0~2
                    tmp += map_1[i+ii][j+jj] #
            if maxv < tmp:
                maxv = tmp
    print("#{}".format(i_test), end=" ")
    print(maxv)