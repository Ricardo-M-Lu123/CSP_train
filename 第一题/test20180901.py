n = int(input())
A = list(map(int, input().split()))
B = {}
for i in range(n):
    if i == 0:  # 第一家
        B[i] = int((A[i] + A[i + 1]) / 2)
    elif i == n - 1:  # 最后一家
        B[i] = int((A[i - 1] + A[i]) / 2)
    else:
        B[i] = int((A[i - 1] + A[i] + A[i + 1]) / 3)
print(" ".join(str(i) for i in B.values()))  # 按空格输出字典的值
