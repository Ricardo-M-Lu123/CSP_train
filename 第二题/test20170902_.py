n,k = map(int,input().split())
key_num = []
use = []
for i in range(n):
    key_num.append(i+1)
for i in range(k):
    w,s,c = map(int,input().split())
    use.append([s,1,w])#1是借
    use.append([s+c,-1,w])#-1是还
use.sort()#默认按第一列排序
for i in range(2*k):
    if use[i][1] == 1:
        key_num[key_num.index(use[i][2])] = 0
    if use[i][1] == -1:
        key_num[key_num.index(0)] = use[i][2]
for i in range(n):
    print(key_num[i],end=' ')