"""
测试用例
3 3
73 -8 -6 -4
76 -5 -10 -8
80 -6 -15 0
"""
N,M=list(map(int,input().split()))
a=[]
b = [0]*N #生成一个包含N个0的序列
for i in range(N):
    x = list(map(int,input().split()))
    t=0
    for j in range(M+1):
        if x[j]>0:
            a.append(x[j])
        else:
            t += x[j]
            b[i]=t
sum = sum(a)+sum(b)
k=0
for i in range(N):
    if abs(b[i])>abs(b[k]):
        k=i
print(sum,k+1,abs(b[k]))
