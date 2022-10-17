# [s,t]表示时间段t-s，代表的是左闭右开区间
n = int(input())
H = [0] * 1000001
W = [0] * 1000001
count = 0
for i in range(n):
    a, b = map(int, input().split())
    for i in range(a, b):
        H[i] = 1
for i in range(n):
    c, d = map(int, input().split())
    for i in range(c, d):
        W[i] = 1
len = max(b, d)
for i in range(0, len):
    if H[i] == 1 & W[i] == 1:
        count += 1
print(count)
