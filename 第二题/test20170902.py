N, K = map(int, input().split())
use = []
keys = []
for i in range(N):
    keys.append(i + 1)
for i in range(K):
    w, s, c = map(int, input().split())
    use.append([s, 1, w])  # 1是借
    use.append([s + c, -1, w])  # -1是还
use.sort()  # 默认按第一列排序
for i in range(2 * K):
    if use[i][1] == 1:
        keys[keys.index(use[i][2])] = 0
    elif use[i][1] == -1:
        keys[keys.index(0)] = use[i][2]
print(" ".join(str(i) for i in keys))
