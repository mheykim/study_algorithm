def solution(genres, plays):
    answer = []
    all_dic = dict({})
    for i in range(len(genres)):
        if genres[i] not in list(all_dic.keys()):
            all_dic[genres[i]] = [[i, plays[i]]]
        else:
            all_dic[genres[i]].append([i, plays[i]])

    play_max = []
    for ii in range(len(all_dic)):
        all_dic[list(all_dic.keys())[ii]].sort(key=lambda x: (-x[1], x[0]))
        # print(all_dic[list(all_dic.keys())[ii]])
        # print(" ")
        sum_val = 0
        for didi in range(len(all_dic[list(all_dic.keys())[ii]])):
            sum_val += all_dic[list(all_dic.keys())[ii]][didi][1]

        play_max.append([sum_val, ii])

    play_max.sort(key=lambda x: -x[0])

    for ii in range(len(play_max)):
        genre_ind = play_max[ii][1]
        if len(all_dic[list(all_dic.keys())[genre_ind]]) == 1:
            answer.append(all_dic[list(all_dic.keys())[genre_ind]][0][0])
        else:
            for compi in range(2):
                answer.append(all_dic[list(all_dic.keys())[genre_ind]][compi][0])

    return answer