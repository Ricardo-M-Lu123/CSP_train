# 　　给定一个年份y和一个整数d，问这一年的第d天是几月几日？
# 　　注意闰年的2月有29天。满足下面条件之一的是闰年：
# 　　1） 年份是4的整数倍，而且不是100的整数倍；
# 　　2） 年份是400的整数倍。

def is_runnian(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 1
    else:
        return 0


year = int(input())
day = int(input())
morth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
r_morth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_runnian(year):
    for i in range(len(r_morth)):
        if day <= r_morth[i]:
            M = i + 1
            D = day
            break
        else:
            day = day - r_morth[i]
else:
    for i in range(len(morth)):
        if day <= morth[i]:
            M = i + 1
            D = day
            break
        else:
            day = day - morth[i]
print(M)
print(D)
