# 별 찍기 - 2

a = int(input())

for i in range(1,a+1):
    print(" " *(a-i) + "*" * i)

    # , 이 아니라 +가 오게 되는 이유는?,,,? 혹시 띄어쓰기 때문?!!