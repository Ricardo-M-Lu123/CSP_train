r, y, g = map(int, input().split())
n = int(input())
k, t = {},{}#list[]为空时，不能用k[i]去赋值；但是{}字典可以用k[i]赋初值！！注意
alltime = 0
for i in range(n):
    k[i], t[i] = list(map(int, input().split()))
    if k[i] == 0:
        alltime += t[i]
    elif k[i] == 1:
        alltime += t[i]
    elif k[i] == 2:
        alltime += t[i] + r
    elif k[i] == 3:
        continue
print(alltime)
# 30 3 30
# 8
# 0 10
# 1 5
# 0 11
# 2 2
# 0 6
# 0 3
# 3 10
# 0 3