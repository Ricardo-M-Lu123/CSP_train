n = int(input())
a = list(map(int, input().split()))
total = 1
for i in range(n - 1):
    if a[i] == a[i + 1]:
        continue
    else:
        total += 1
print(total)
