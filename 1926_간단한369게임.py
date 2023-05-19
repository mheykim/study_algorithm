N = int(input())
ans = []
for num in range(1, N+1):
    num_s = str(num)
    count_3 = num_s.count("3")
    count_6 = num_s.count("6")
    count_9 = num_s.count("9")
    if count_3 > 0 or count_6 > 0 or count_9 > 0:
        ans.append("-"*(count_3+count_6+count_9))
    else:
        ans.append(num_s)
print(" ".join(ans))