n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(1, n - 1):
    if (a[i] - a[i - 1]) * (a[i] - a[i + 1]) > 0:
        count += 1
    else:
        continue
print(count)
