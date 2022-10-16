# 输入
# 10 7
# 1 2
# 3 3
# 3 0
# 3 3
# 6 2
# 2 1
# 8 2
#输出
# 3

n,k=map(int,input().split())
# a=[]
a=set()
count=0
for i in range(0,k):
    x,y=map(int,input().split())
    if (y!=0) & (y not in a):
        count+=1
    # a.append(x)
    a.add(x)
print(count)
