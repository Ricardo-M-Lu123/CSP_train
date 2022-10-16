# n = int(input())
# a = list(map(int, input().split()))
# res = 100000000
# for i in range(n):
#     for j in range(i + 1, n):
#         chazhi = abs(int(a[i]) - int(a[j]))
#         if chazhi < res:
#             res = chazhi
# print(res)


n = int(input())
a = list(map(int, input().split()))
res = 100000000
a.sort()
for i in range(n-1):
    chazhi = abs(a[i] - a[i+1])
    if chazhi < res:
        res = chazhi
print(res)