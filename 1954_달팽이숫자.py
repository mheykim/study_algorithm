T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def draw(N):
    map_1 = [[0]*N for _ in range(N)]
    len_one = N
    dir = 0
    ey, ex = 0, -1
    count = 1

    for li in range(len_one):
        ey = ey + dy[dir]
        ex = ex + dx[dir]
        map_1[ey][ex] = count
        count += 1

    dir = (dir + 1) % 4
    len_one -= 1

    while True:
        for li in range(len_one):
            ey = ey + dy[dir]
            ex = ex + dx[dir]
            map_1[ey][ex] = count
            count += 1

        dir = (dir+1)%4

        for li in range(len_one):
            ey = ey + dy[dir]
            ex = ex + dx[dir]
            # try:
            map_1[ey][ex] = count
            # except:
            #     print("")
            count += 1

        dir = (dir + 1) % 4
        len_one -= 1

        if count > N*N:
            break

    for i in range(N):
        print(" ".join(list(map(str, map_1[i]))))


for test_i in range(T):
    N = int(input())
    print("#{}".format(test_i+1))
    draw(N)
