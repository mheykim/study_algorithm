T = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

from collections import deque

def dfs(ey, ex, count, line):
    global map_1, ans
    if count == 7 :
        cand = "".join(list(map(str, line)))
        # if cand not in ans:
        ans.append(cand)
        return

    for di in range(4):
        ny = ey + dy[di]
        nx = ex + dx[di]
        if not(0<=nx<4 and 0<=ny<4):
            continue
        dfs(ny, nx, count+1, line + [map_1[ny][nx]])


for i_test in range(1, T+1):
    map_1 = [list(map(int, input().split())) for _ in range(4)]
    ans = []
    for j in range(4):
        for i in range(4):
            dfs(j, i, 0, []) # y, x, count

    print("#{}".format(i_test), end = " ")
    ans = set(ans)
    print(len(ans))