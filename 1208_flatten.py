def dump():
    global box_info
    maxv = max(box_info)
    maxv_ind = box_info.index(maxv)
    minv = min(box_info)
    minv_ind = box_info.index(minv)
    if maxv == minv or maxv-minv == 1:
        return False
    box_info[maxv_ind] -= 1
    box_info[minv_ind] += 1
    return 1

for test_i in range(1, 11):
    n_dump = int(input())
    box_info = list(map(int, input().split()))
    # box_info.sort(reverse=True)

    for dump_i in range(n_dump):
        ans = dump()
        if ans == False:
            # ans = max(box_info) - min(box_info)
            break

    print("#{}".format(test_i), end=" ")
    print(max(box_info) - min(box_info))
