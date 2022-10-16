n,m = map(int,input().split())
p=[]
l=[]
for _ in range(n):
    p.append(input().split())
for _ in range(m):
    l.append(list(map(int, input().split())))
for i in range(m):
    az=0
    af=0
    bz=0
    bf=0
    for j in range(n):
        re = l[i][0]+l[i][1]*int(p[j][0])+l[i][2]*int(p[j][1])
        if (re>0)&(p[j][2]=='A'):
            az=az+1
        elif (re<0)&(p[j][2]=='A'):
            af=af+1
        elif (re>0)&(p[j][2]=='B'):
            bz=bz+1
        elif (re<0)&(p[j][2]=='B'):
            bf=bf+1
    if ((az+bf)==n)|((af+bz)==n):
        print('Yes')
    else:
        print('No')

