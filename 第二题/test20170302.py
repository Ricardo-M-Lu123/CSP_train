people_num = int(input())
people = []
for i in range(people_num):
    people.append(i + 1)
opp_num = int(input())
opp = []
for i in range(opp_num):
    a, b = list(map(int, input().split()))
    opp.append((a, b))
for i in range(opp_num):
    number_idx = people.index(opp[i][0])  # 列表获取索引
    people.remove(opp[i][0])  # 列表删除元素
    people.insert(number_idx + opp[i][1], opp[i][0])  # 列表在idx位置插入元素
print(" ".join(str(i) for i in people))
