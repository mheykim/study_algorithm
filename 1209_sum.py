for test_i in range(1, 11):
    t = int(input())
    map_1 = [list(map(int, input().split()))for _ in range(100)]
    maxv = 0
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += map_1[j][i]
        maxv = max(tmp, maxv)

    for j in range(100):
        tmp = 0
        for i in range(100):
            tmp += map_1[j][i]
        maxv = max(tmp, maxv)

    tmp = 0
    for i in range(100):
        tmp += map_1[i][i]
    maxv = max(tmp, maxv)

    tmp = 0
    for i in range(100):
        tmp += map_1[i][99-i]
    maxv = max(tmp, maxv)

    print("#{}".format(t), end=" ")
    print(maxv)