# n = 6
# B = [0,0,5,5,10,10]

n = input()
B = []
B = list(map(int, input().split()))

sum_min = B[0]
sum_max = B[0]
for i in range(1,len(B)):
    if B[i] == B[i-1]:
        sum_max = sum_max + B[i-1]
        sum_min = sum_min + 0
    else:
        sum_max = sum_max + B[i]
        sum_min = sum_min + B[i]
print(sum_max)
print(sum_min)