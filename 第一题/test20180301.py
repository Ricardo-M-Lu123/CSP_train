a = list(map(int, input().split()))
len = len(a)
leiji = 0  # 用来存放累计跳中心的加分
count = 0  # 用来存放总分
for i in range(len):
    if a[i] == 1:
        count += 1
        leiji = 0
    elif a[i] == 2:
        if a[i - 1] == 1 or i == 0:
            count += 2
            leiji += 2
        elif a[i - 1] == 2:
            count += leiji + 2
            leiji += 2
    elif a[i] == 0:
        break
print(count)
# 1 1 2 2 2 1 1 2 2 0
