n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
c=[]
c.append(1)
for i in range(n):#更新c
    A=c[i]*a[i]
    c.append(A)
for i in range(1,n+1):
    b.append((m%c[i]-m%c[i-1])/c[i-1])
for i in range(n):
    print(int(b[i]),end=" ")

#15 32767
# 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2