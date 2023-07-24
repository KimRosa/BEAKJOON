# 영수증

a = int(input())
n = int(input())
sum = 0

for i in range(n):
    b,c = map(int, input().split())
    sum += (b*c)

if a == sum:
    print("Yes")

else:
    print("No")
