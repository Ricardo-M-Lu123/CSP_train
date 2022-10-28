# 消除游戏

n, m = map(int, input().split())
A = [[0] * m for _ in range(n)]  # 生成二维数组一定要用这个形式！！！！！！
come = [[0] * m for _ in range(n)]
for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(n):  # 按列比较
    for j in range(m - 2):
        if A[i][j] == A[i][j + 1] and A[i][j] == A[i][j + 2]:
            come[i][j] = A[i][j]
            come[i][j + 1] = A[i][j + 1]
            come[i][j + 2] = A[i][j + 2]
for j in range(m):  # 按行比较
    for i in range(n - 2):
        if A[i][j] == A[i + 1][j] and A[i][j] == A[i + 2][j]:
            come[i][j] = A[i][j]
            come[i + 1][j] = A[i + 1][j]
            come[i + 2][j] = A[i + 2][j]
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        result[i][j] = A[i][j] - come[i][j]
        print(result[i][j], end=" ")
    print("\r")  # \n换行,\r回车
