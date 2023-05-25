n = int(input())
k = int(input())
loc_apple = [list(map(int, input().split())) for _ in range(k)]
map1 = [[0]*n for _ in range(n)]
for i in range(k):
    for j in range(2):
        loc_apple[i][j] -= 1

for j in range(n):
    for i in range(n):
        if [j, i] in loc_apple:
            map1[j][i] = 1

l = int(input())

snake_head = [0, 0]
snake_tail = [0, 0]
length_snake = 1
body = [[0, 0]]
# 0 = R, 1 = U, 2 = L, 3 = D
dx = [1, 0, -1, 0] # 우 상 좌 하
dy = [0, -1, 0, 1] # L: (4 + 방향 +1)%4, R: (4 + 방향-1)%4
t_global = 0


def init_move(t):
    global snake_head, snake_tail, t_global, length_snake
    ehx = snake_head[0]
    ehy = snake_head[1]
    etx = snake_tail[0]
    ety = snake_tail[1]

    while t_global < t:
        nhx = ehx + dx[0]
        nhy = ehy + dy[0]
        if nhx == n or nhx == -1 or nhy ==n or nhy ==-1 : # 벽에 닿음
            flg = True
            return(t_global)

        if [nhx, nhy] in body :
            flg = True
            return(t_global)

        if map1[nhy][nhx] ==1: # 사과 있을 때
            map1[nhy][nhx] = 0
            length_snake +=1
            # check_body[nhy][nhx] = True
            body.append([nhx, nhy])
            ehx = nhx
            ehy = nhy

        else:
            ehx = nhx
            ehy = nhy
            body.append([nhx, nhy])
            etx, ety = body.pop(0)


        t_global+=1

    snake_head = [ehx, ehy]
    snake_tail = [etx, ety]
    return

def move(t, d): # x = x초 후 움직임 시작, c = Direction
    global snake_head, snake_tail, t_global, length_snake, dir_snake, flg

    ehx = snake_head[0]
    ehy = snake_head[1]
    etx = snake_tail[0]
    ety = snake_tail[1]

    d_next = dir_snake
    if d == 'L':
        d_next = (4 + dir_snake + 1) % 4

    elif d == 'D':
        d_next = (4 + dir_snake - 1) % 4
    dir_snake = d_next
    while t_global < t:

        nhx = ehx + dx[dir_snake]
        nhy = ehy + dy[dir_snake]

        if nhx == n or nhx == -1 or nhy == n or nhy == -1:  # 벽에 닿음
            flg = True
            return t_global

        if [nhx, nhy] in body:
            flg = True
            return(t_global)

        if map1[nhy][nhx] == 1:  # 사과 있을 때
            map1[nhy][nhx] = 0
            length_snake += 1
            body.append([nhx, nhy])
            ehx = nhx
            ehy = nhy

        else:
            ehx = nhx
            ehy = nhy
            body.append([nhx, nhy])

            etx, ety = body.pop(0)


        t_global += 1

    snake_head = [ehx, ehy]
    snake_tail = [etx, ety]
    return

dir_snake = 0
x_list = []
c_list = []
for _ in range(l):
    x, c = input().split()
    x_list.append(int(x))
    c_list.append(str(c))

x_list.append(999999999)

flg = False
for i in range(len(x_list)):
    t_til = x_list[i]
    if i == 0 :
        init_move(t_til)
    else:
        move(t_til, c_list[i-1])
    if flg : break

print(t_global+1)


