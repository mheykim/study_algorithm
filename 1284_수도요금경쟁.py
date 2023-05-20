T = int(input())
for test_i in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A_fee = W*P
    B_fee = Q
    if W > R:
        B_fee += (W-R)*S
    ans = min(A_fee, B_fee)
    print("#{}".format(test_i), end=" ")
    print(ans)