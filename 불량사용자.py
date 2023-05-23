from itertools import permutations


def check(unit, ban):
    for i in range(len(unit)):
        if len(unit[i]) != len(ban[i]):  # 가져온 tuple과 banned_id의 길이가 맞지않는다면 종료
            return False
        for j in range(len(unit[i])):  # tuple의 스펠과 baaned_id가 맞지않는다면 종료, "*"는 그대로 진행
            if unit[i][j] != ban[i][j] and ban[i][j] != "*":
                return False

    return True


def solution(user_id, banned_id):
    answer = []
    print(list(permutations(user_id, len(banned_id))))
    for unit in permutations(user_id, len(banned_id)):  # permutations에서 tuple을 한개씩 가져온다
        if check(unit, banned_id):
            if set(unit) not in answer:  # 겹치는지 판별
                answer.append(set(unit))

    return len(answer)  # 중복값이 제거된 answer의 길이출력