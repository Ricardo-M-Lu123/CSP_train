n = int(input())
a = list(map(int, input().split()))  # 输入一个序列按空格分隔
ave = 0
A = 0
D = 0
S = 0
for i in range(n):
    A += a[i]
ave = A / n
for i in range(n):
    S += (a[i] - ave) ** 2
D = S / n
B = []
for i in range(n):
    B.append((a[i] - ave) / pow(D, 0.5))  # pow(D,0.5)开根号的意思 (D**0.5)也是开根号的意思
    print(B[i])
