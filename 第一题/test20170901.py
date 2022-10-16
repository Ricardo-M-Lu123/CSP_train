N = int(input())
total = 0
while (N):
    if int(N / 50) != 0:
        total += 7 * int(N / 50)
        N = N % 50
    elif int(N / 30) != 0:
        total += 4 * int(N / 30)
        N = N % 30
    else:
        total += 1 * int(N / 10)
        N = N % 10
print(total)
