def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    flg = False
    for i in range(1, n):
        if [1, i + 1] in puddles:
            flg = True
        if flg:
            dp[i][0] = 0
            continue
        dp[i][0] = 1

    flg = False
    for j in range(1, m):
        if [j + 1, 1] in puddles:
            flg = True
        if flg:
            dp[0][j] = 0
            continue
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [j + 1, i + 1] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    answer = dp[n - 1][m - 1] % 1000000007
    # print(dp)
    return answer