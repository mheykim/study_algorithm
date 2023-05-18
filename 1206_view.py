for test_i in range(1, 11):
    N = int(input())
    apt = list(map(int, input().split()))
    ans = 0
    for i in range(2, N-2):
        left_maxv = max(apt[i-1], apt[i-2])
        right_maxv = max(apt[i+1], apt[i+2])
        if left_maxv < apt[i] and right_maxv < apt[i]:
            maxmax = max(left_maxv, right_maxv)
            ans += apt[i] - maxmax
    print("#{}.".format(test_i), end=" ")
    print(ans)