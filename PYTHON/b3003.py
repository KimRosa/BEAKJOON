# 킹, 퀸, 룩, 비숍, 나이트, 폰
chess = list(map(int, input().split()))
orign = [1, 1, 2, 2, 2, 8]
for i in range(6):
    print(orign[i] - chess[i], end=" ")
