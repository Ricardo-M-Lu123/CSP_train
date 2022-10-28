n = int(input())
figure = [[0] * 100 for _ in range(100)]#生成二维数组一定要用这个形式！！！
for k in range(n):
    x1, y1, x2, y2 = list(map(int, input().split()))
    for i in range(x1, x2):
        for j in range(y1, y2):
            figure[i][j] += 1
count = 0
for i in range(100):
    for j in range(100):
        if figure[i][j] != 0:
            count += 1
print(count)
