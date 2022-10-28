#只得了90分，超时

n, k = map(int, input().split())
children = []
for i in range(n):
    children.append(i + 1)
number = 1
while (children.count(0) != n - 1):
    for child, i in zip(children, range(n)):
        if child != 0 and number % k != 0 and number % 10 != k:
            number += 1
            continue
        elif child == 0:
            continue
        elif child != 0 and (number % k == 0 or number % 10 == k):
            number += 1
            children[i] = 0
print(children[[i for i, e in enumerate(children) if e != 0][0]])
# for i in range(n):
#     if children[i] != 0:
#         print(children[i])
