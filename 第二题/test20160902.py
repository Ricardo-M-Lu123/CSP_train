# 输入购票指令次数
n = int(input())
# 初始化火车座位状态列表
seat = [0 for i in range(100)]
# 记录每行座位空位数量列表
row = [5 for i in range(20)]
# 输入购买指令
ticket = list(map(int,input().split()))
# 循环输入
for x in ticket:
    # 选到连续座位标记
    complete = False
    # 遍历每行(空位数量)
    for j in range(20):
        # 当此行空位足够
        if row[j] >= x:
            count = 0 # 已选计数器
            # 选择x个作座位并输出
            for k in range(5):
                if seat[j*5+k] == 0:
                    seat[j*5+k] = 1
                    count += 1
                    print(j*5+k+1,end=" ")
                if count == x:
                    print()
                    break
            # 更新当前排的座位数
            row[j] -= x
            complete = True
            break
    # 当车厢内不存在连续的座位
    count = 0 #　已选座位计数器
    i = 0 # 座位序号
    # 选择x个作座位并输出
    while complete == False:
        # 当此时为空座 选中该座位输出 更新当前排的座位数
        if seat[i] == 0:
            seat[i] = 1
            row[int(i/5)] -= 1
            count += 1
            print(i+1,end=" ")
        if count == x:
            print()
            complete = True
        i += 1
