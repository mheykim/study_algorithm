
T = int(input())
for test_i in range(T):
    N = int(input())
    line = list(map(int, input().split()))
    ans = 0
    maxv = line[N-1]
    for i in range(N-1, -1, -1):
        if line[i] < maxv:
            ans += maxv - line[i]
        elif line[i] == maxv:
            pass
        else: # line[i] > maxv
            maxv = line[i]

    print("#{}".format(test_i+1), end=" ")
    print(ans)