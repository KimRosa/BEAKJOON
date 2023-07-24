# 주사위 세개
# 조건에 따라 상금을 계산하는 문제

a,b,c = map(int, input().split())

if a==b and b==c:
    print(10000 + (a*1000))

elif a==b and b!=c:
    print(1000+ (a*100))

elif a!=b and b==c:
    print(1000+ (b*100))

elif a==c and b!=c:
    print(1000+ (a*100))

else:
    print(max(a,b,c)*100)
    
 