T = int(input())
for test_i in range(1, T+1):
    N = int(input())
    print("#{}".format(test_i))
    if N == 1:
        print(1)
        continue
    elif N == 2:
        print(1)
        print("1 1")
        continue
    else:
        ans = [[0]*N for _ in range(N)]
        ans[0][0] = 1
        ans[1][0] = 1
        ans[1][1] = 1
        for ii in range(2, N):
            ans[ii][0] = 1
            ans[ii][ii] = 1

        for i in range(2, N):
            for j in range(1, N):
                if i == j : continue
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

        for i in range(N):
            tmp = ans[i][:i+1]
            print(" ".join(list(map(str,tmp))))
