def solution(n, edge):
    answer = 0
    edge.sort()
    edges = [[] for _ in range(n)]
    for i_edge in range(len(edge)):
        edges[edge[i_edge][0] - 1].append(edge[i_edge][1] - 1)
        edges[edge[i_edge][1] - 1].append(edge[i_edge][0] - 1)
    check_arr = [0] * n
    check_arr[0] = 1
    distance = [0] * n
    distance[0] = 1
    from collections import deque
    q = deque([])
    q.append(0)
    while len(q) > 0:
        current_edge = q.popleft()

        for next_edge in edges[current_edge]:
            if check_arr[next_edge]:
                distance[next_edge] = min(distance[current_edge] + 1, distance[next_edge])
            else:
                distance[next_edge] = distance[current_edge] + 1
                check_arr[next_edge] = 1
                q.append(next_edge)
    distance.sort(reverse=True)
    maxv = max(distance)
    for i in range(len(distance)):
        if distance[i] == maxv:
            answer += 1
        else:
            break
    return answer