n,m = map(int, input().split())

basket = [0]*n

for _ in range(m):
    i,j,k = map(int, input().split())
    
    for x in range(i, j+1):
        basket[x-1] = k

print(*basket)


# 리스트 앞에 *을 붙이면 리스트를 언패킹해서 출력할 수 있게 해준다.
# print(basket) == [1,2,3,4,5]
# print(*basket) == 1,2,3,4,5
   
    
                
