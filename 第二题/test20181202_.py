#以绿色为开始，绿黄红，周期为T，now%T，判断是否在<g的区间里，若小于则直行，否则判断now是周期的哪个时刻，alltime+=T-now
#核心思想：now时刻的表达
r, y, g = map(int, input().split())
n = int(input())
alltime = 0
now = 0
T = r + g + y
for i in range(n):
    k, t = map(int, input().split())
    if k == 0:
        alltime += t
    elif k == 1:
        now = g + y + r - t + alltime
        now = now % T
        if now > g:
            alltime += T - now
    elif k == 2:
        now = g + y - t + alltime
        now = now % T
        if now > g:
            alltime += T - now
    elif k == 3:
        now = g - t + alltime
        now = now % T
        if now > g:
            alltime += T - now
print(alltime)
