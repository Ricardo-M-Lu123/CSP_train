n = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(n):
    if -a[i] in a:
        count += 1
print(int(count / 2))
