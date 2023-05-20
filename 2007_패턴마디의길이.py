T = int(input())
for test_i in range(1, T+1):
    line = list(map(str, input()))
    whole = "".join(line)
    tmp = line[0]
    for i in range(1, 10):
        next_tmp = line[len(tmp):len(tmp)*2]
        if tmp == "".join(next_tmp):
            break
        tmp += line[i]

    ans = len(tmp)
    print("#{}".format(test_i), end=" ")
    print(ans)