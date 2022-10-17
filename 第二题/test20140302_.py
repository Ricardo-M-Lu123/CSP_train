#判别函数
#  点击位置click_position落在窗口window内吗
def is_in(click_position, window):
    x, y = click_position
    x1, y1, x2, y2 = window[1]
    return x1<=x<=x2  and y1<=y<=y2  #题意保证x1<x2, y1<y2

N, M = [int(s) for s in input().split()]
windows = []
for i in range(N):
    window = [int(s) for s in input().split()]
    windows.append((i+1, window))  #i+1是窗口编号

for i in range(M):
    x, y = [int(s) for s in input().split()]
    # print(windows)
    for j in range(N-1, -1, -1):  #windows从右到左，对应窗口从顶层到底层
        if is_in((x, y), windows[j]):
            print(windows[j][0])
            #！！！更新点击到的窗口，置于上位。如何做：先.pop()删除该元素并利用window返回元素，后面再将window加进来
            window = windows.pop(j)  #注意：列表元素增减会干扰for循环的执行。
            windows.append(window)  #这里，列表元素调换位置，而后break跳出，无需担心干扰。
            break  #break跳出for语句，不会执行下面的else分支
    else:  #python语言中，for, while语句可以有else分支。
        print("IGNORED")    #else分支在循环条件不成立导致循环结束后执行。
