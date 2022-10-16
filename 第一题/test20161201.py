n = int(input())
a = list(map(int, input().split()))
mincount = 0
maxcount = 0
a.sort()
if n % 2 == 0:  # 偶数
    i = int(n / 2 - 1)
    if a[i] != a[i + 1]:
        print(-1)
    else:
        mid = a[i]
        for i in range(n):
            if a[i] < mid:
                mincount += 1
            elif a[i] > mid:
                maxcount += 1
        if mincount == maxcount:
            print(mid)
        else:
            print(-1)
else:  # 奇数
    i = int(n / 2)
    mid = a[i]
    for i in range(n):
        if a[i] < mid:
            mincount += 1
        elif a[i] > mid:
            maxcount += 1
    if mincount == maxcount:
        print(mid)
    else:
        print(-1)
