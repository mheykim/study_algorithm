T = int(input())
for iii in range(T):
    t = int(input())
    scores = list(map(int, input().split()))
    l = [0]*101
    for i in range(1000):
        l[scores[i]-1] += 1

    maxv = -1
    max_ind = -99
    for ii in range(len(l)-1, -1, -1):
        if maxv < l[ii]:
            maxv = l[ii]
            max_ind = ii
    # maxv = max(l)
    # max_ind = l.index(maxv)
    print("#{}".format(t), end=" ")
    print(max_ind+1)
