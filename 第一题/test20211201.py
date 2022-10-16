##使用map()函数可以实现将其他类型的数转换成list
n, N = map(int,input().split())#n是输入个数，N是序列里最大整数不能超过的值
a = []
a = list(map(int, input().split()))
a.insert(0,0)
sum = 0
f_i = 0
for i in range(1, len(a)):
    sum = sum + (a[i]-a[i-1]) * f_i
    f_i = f_i + 1
sum = sum + (N - a[len(a)-1]) * f_i
print(sum)