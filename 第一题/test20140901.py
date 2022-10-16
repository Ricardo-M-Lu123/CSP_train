n = int(input())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range(n):
    if a[i] + 1 in a:
        count += 1
print(count)
