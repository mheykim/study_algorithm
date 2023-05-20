from collections import deque

def check():
    global ans, map_1
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for j in range(16):
        for i in range(16):
            if map_1[j][i] == 2:
                y_start, x_start = j, i
            elif map_1[j][i] == 3:
                y_end, x_end = j, i
    q = deque([])
    check_arr = [[False]*16 for _ in range(16)]
    q.append([y_start, x_start])
    check_arr[y_start][x_start]

    while len(q)>0:
        ey, ex = q.popleft()
        if [ey, ex] == [y_end, x_end]:
            ans = 1
            return

        for di in range(4):
            ny = ey + dy[di]
            nx = ex + dx[di]
            if not(0<=ny<16 and 0<=nx<16):
                continue
            if check_arr[ny][nx]:
                continue
            if map_1[ny][nx] == 1:
                continue
            check_arr[ny][nx] = True
            q.append([ny, nx])


for _ in range(10):
    t = int(input())
    map_1 = [list(map(int, input())) for _ in range(16)]
    ans = 0
    check()
    print("#{}".format(t), end=" ")
    print(ans)