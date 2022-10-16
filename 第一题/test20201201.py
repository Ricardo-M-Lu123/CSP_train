n = int(input())
w = []
score = []
ReLu = 0
for i in range(0,n):
    w, score = map(int, input().split())
    ReLu = ReLu + w*score
if ReLu < 0:
    print(0)
else:
    print(ReLu)
