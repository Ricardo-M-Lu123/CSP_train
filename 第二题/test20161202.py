T = int(input())
wage_level = {"A": 3500,
              "B": 3500 + 1500 * 0.97,
              "C": 3500 + 1500 * 0.97 + 3000 * 0.9,
              "D": 3500 + 1500 * 0.97 + 3000 * 0.9 + 4500 * 0.8,
              "E": 3500 + 1500 * 0.97 + 3000 * 0.9 + 4500 * 0.8 + 26000 * 0.75,
              "F": 3500 + 1500 * 0.97 + 3000 * 0.9 + 4500 * 0.8 + 26000 * 0.75 + 20000 * 0.7,
              "G": 3500 + 1500 * 0.97 + 3000 * 0.9 + 4500 * 0.8 + 26000 * 0.75 + 20000 * 0.7 + 25000 * 0.65
              }
# print(wage_level)
if T <= 3500:  # level:A
    S = T
elif 3500 < T <= 4955:  # level:B
    S = (T - wage_level["A"]) / 0.97 + 3500
elif 4955 < T <= 7655:  # level:C
    S = (T - wage_level["B"]) / 0.9 + 5000  # 在B之前的，B已经上过税了，所以直接加达到B等级的5000就好了，在B C等级之间的税后钱（即T- wage_level["B"]）除以税率
elif 7655 < T <= 11255:  # level:D
    S = (T - wage_level["C"]) / 0.8 + 8000
elif 11255 < T <= 30755:  # level:E
    S = (T - wage_level["D"]) / 0.75 + 12500
elif 30755 < T <= 44755:  # level:F
    S = (T - wage_level["E"]) / 0.7 + 38500
elif 44755 < T <= 61005:  # level:G
    S = (T - wage_level["F"]) / 0.65 + 58500
elif 61005 < T:
    S = (T - wage_level["G"]) / 0.55 + 83500
print(int(S))
