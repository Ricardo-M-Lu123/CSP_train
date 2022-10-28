# 用while(len(children)>1):去判断是否继续报数，到只剩最后一个孩子时停止
# 每遍历一轮list，就删一批被淘汰的人

n, k = map(int, input().split())
children = []
for i in range(n):
    children.append(i + 1)
count = 0
# 设计一个放移出人的list
remove_children = []
while (len(children) > 1):
    for i in range(len(children)):
        count += 1
        if count % k == 0 or count % 10 == k:
            remove_children.append(children[i])
    for i in range(len(remove_children)):
        children.remove(remove_children[i])
        if len(children) == 1:  # 如果提前就只剩下一个小朋友了，就直接退出。以防k=1，剩下10和11都被删掉的情况
            break
    remove_children = []
print(children[0])
