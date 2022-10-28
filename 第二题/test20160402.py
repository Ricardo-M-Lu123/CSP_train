from copy import deepcopy

map0 = []
map1=[]
for i in range(15):
    a = list(map(int, input().split()))
    map0.append(a)
map1=deepcopy(map0)
square = [[0] * 4 for _ in range(4)]
for i in range(4):
    square[i] = list(map(int, input().split()))
star = int(input())
for k in range(0, 15):
    result = []
    result=deepcopy(map0)
    if k == 0:
        for j, j0 in zip(range(star - 1, star + 3), range(4)):
            result[0][j] = map1[0][j] + square[3][j0]

    elif k == 1:
        for i in range(0, 2):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[3 - i][j0]

    elif k == 2:
        for i in range(0, 3):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[3 - i][j0]

    elif k == 3:
        for i in range(0, 4):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[3 - i][j0]

    elif k==12:
        for i in range(k, k+3):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[i-k][j0]
        for aaa in result:
            if 2 not in aaa:
                result_back = []
                result_back = deepcopy(result)
        else:
            break
    elif k==13:
        for i in range(k, k+2):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[i-k][j0]

    elif k==14:
        for i in range(k, k+1):
            for j, j0 in zip(range(star - 1, star + 3), range(4)):
                result[i][j] = map1[i][j] + square[i-k][j0]

    else:
        for j, j0 in zip(range(star - 1, star + 3), range(4)):
            for i, i0 in zip(range(k, k+4), range(4)):
                result[i][j] =map1[i][j]+square[i0][j0]

    for aaa in result:
        if 2 in aaa:
            break
    else:
        result_back = []
        result_back = deepcopy(result)

for i in range(15):#用空格按行输入
    print(" ".join(str(j) for j in result_back[i]))