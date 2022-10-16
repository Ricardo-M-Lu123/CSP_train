n, m = map(int, input().split())
line = [[0] * m] * n  # 初始化二维数组  每行m个元素共n行
for i in range(n):
    line[i] = input().split(" ")  # 输入二维数组，同行数字用空格分隔，不同行则用回车换行
res0 = [[0] * n for _ in range(m)] #生成m*n的二维数组
for i in range(n):
    for j in range(m):
        res0[j][i] = line[i][m - j - 1]
for i in range(m):
    print(" ".join(str(int(i)) for i in res0[i]))
