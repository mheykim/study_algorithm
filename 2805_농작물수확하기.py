T = int(input())
for i_test in range(1, T+1):
    N = int(input())
    ans = 0
    map_1 = [list(map(int, input())) for _ in range(N)]
    if N == 1:
        ans = map_1[0][0]
    else:
        x_mid, y_mid = N//2, N//2
        for i in range(N): # 가운데
            ans += map_1[y_mid][i]
        tmp = []
        for i in range(N//2): # 위
            tmp.append(sum(map_1[i][x_mid-i : x_mid+i+1]))

        for i in range(N-1, N//2, -1): # 아래
            tmp.append(sum(map_1[i][x_mid-(N-1-i) : x_mid+(N-1-i)+1]))
        ans += sum(tmp)


    print("#{}".format(i_test), end=" ")
    print(ans)