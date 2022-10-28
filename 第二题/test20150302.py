n = int(input())
A = list(map(int, input().split()))
B = [0] * 1001  # 注意！！1001才是0~1000，1000个元素的话包含不到1000
result = []
for i in range(n):
    B[A[i]] += 1
for i in range(len(set(A))):
    result.append((B.index(max(B)), max(B)))  # B.index(max(B))求B对应最大元素的索引值
    B[B.index(max(B))] = 0  # 输出之后设成0，以免影响后面的判断
for i in range(len(result)):
    print(result[i][0], result[i][1])
