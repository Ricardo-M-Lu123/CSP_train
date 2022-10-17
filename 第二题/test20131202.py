a = list(map(str, input()))
b = list(filter(str.isdigit, a))  # 提取字符序列里的数
if a[-1]=='X':
    b.append('X')
sum = 0
for i in range(len(b) - 1):
    sum += int(b[i]) * (i + 1)
yushu = sum % 11
if yushu == 10:
    yushu = 'X'
if str(yushu) == a[len(a) - 1]:
    print("Right")
else:
    print("".join(str(i) for i in a[:-1]) + str(yushu))
