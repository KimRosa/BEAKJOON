# 문자열 반복

t = int(input())

for _ in range(t):
    r, s = input().split()
    for p in s:
        print(int(r) * p, end="")
    print("")
