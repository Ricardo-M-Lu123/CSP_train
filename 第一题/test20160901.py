n = int(input())
a = list(map(int, input().split()))
div = 0
max = 0
for i in range(n - 1):
    div = abs(a[i] - a[i + 1])
    if div > max:
        max = div
print(max)
