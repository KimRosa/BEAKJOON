# 오븐 시계
# 범위가 더 넓은 시간 계산 문제

h,m = map(int, input().split())
t = int(input())

h += t//60
m += t%60

if m>=60:
    h = h+1
    m = m-60
    
if h>=24:
    h = h-24



print(h,m)

