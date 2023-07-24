# 공 바꾸기

n,m = map(int, input().split())
num = [i for i in range(1,n+1)]
temp = 0

for _ in range(m):
    i,j = map(int, input().split())
    temp = num[i-1]
    num[i-1] = num[j-1]
    num[j-1] = temp

for i in num:
    print(i, end=" ")
