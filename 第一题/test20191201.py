n = input()
i = 1
count = 1
A = [0,0,0,0]
while count <= int(n):
    if (i%7 == 0)|('7' in str(i)):  #((i-int(i/10)*10)==7)|(int(i/10)==7)|(int(i/100)==7):
        if i%4 == 1:
            A[0]=A[0]+1
            i=i+1
            continue
        if i%4 == 2:
            A[1]=A[1]+1
            i=i+1
            continue
        if i%4 == 3:
            A[2]=A[2]+1
            i=i+1
            continue
        if i%4 == 0:
            A[3]=A[3]+1
            i=i+1
            continue
    else:
        count=count+1
        i = i + 1
print(int(A[0]))
print(int(A[1]))
print(int(A[2]))
print(int(A[3]))

