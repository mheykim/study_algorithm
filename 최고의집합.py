def solution(n, s):
    answer = []
    cand = []
    tmp = s // n
    tmp2 = s % n
    if tmp == 0:
        ans = [-1]
        return ans

    for i in range(n - tmp2):
        cand.append(tmp)
    if tmp2 > 0:
        for i in range(tmp2):
            cand.append(tmp + 1)

    # print(cand)
    return cand