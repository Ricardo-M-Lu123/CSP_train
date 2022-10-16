n = int(input())
a = list(map(int, input().split()))
b = [0] * n
reader = [0] * n
for i in range(n):
    reader[a[i]] += 1
    b[i] = reader[a[i]]
print(" ".join(str(i) for i in b))
