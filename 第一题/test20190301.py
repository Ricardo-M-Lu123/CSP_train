# 4
# -2 -1 3 4
n = int(input())
A = list(map(int, input().split()))
if n % 2 == 0:  # 偶数
    mid = (A[int(n / 2)] + A[int(n / 2 - 1)]) / 2
else:
    mid = A[int((n - 1) / 2)]
if A[0] > A[1]:  # 降序
    min = A[n - 1]
    max = A[0]
else:
    max = A[n - 1]
    min = A[0]
if mid % 1 == 0:  # 判断mid是否为整数
    print(max, int(mid), min)
else:
    print(max, round(mid, 1), min)
