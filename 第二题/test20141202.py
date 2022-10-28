# 4
# 1 5 3 9
# 3 7 5 6
# 9 4 6 4
# 7 3 1 3
n = int(input())
A = [[] * n] * n  # 初始化一个二维数组
result = []
for i in range(n):  # 用空格按行输入
    A[i] = input().split(" ")
for i in range(0, n):
    if i % 2 == 1:  # 奇数
        for j in range(0, i + 1):
            result.append(A[j][i - j])
    else:
        for j in range(0, i + 1):
            result.append(A[i - j][j])
for i in range(n, 2 * n):
    if i % 2 == 1:
        for j in range(i - n + 1, n):
            result.append(A[j][i - j])
    else:
        for j in range(i - n + 1, n):
            result.append(A[i - j][j])
for i in range(len(result)):
    print(int(result[i]), end=" ")
