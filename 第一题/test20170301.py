n, k = map(int, input().split())
a = list(map(int, input().split()))
total = 0
num = 1
i = 1
total += a[0]
while (i < n):
    if total >= k:
        total = 0
        num += 1
        # i += 1
    elif total < k & i == n - 1:
        num += 1
    else:
        total += a[i]
        i += 1
print(num)
