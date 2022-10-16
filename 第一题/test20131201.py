n = int(input())
a = list(map(int, input().split()))
b = [0] * 10000
for i in range(n):
    b[a[i]] += 1
print(b.index(max(b)))
