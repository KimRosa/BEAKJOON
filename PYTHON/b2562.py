# 최댓값

num_list = []       # 입력받을 공갈리스트 만들어주고

for i in range(9):      #9개 받을 거라고 했으니
    num_list.append(int(input()))       #입력 받은 값 공갈리스트에 넣어준다

print(max(num_list))        # 리스트의 max값 출력하고
print(num_list.index(max(num_list))+1)      # 리스트 위치 알려주는 index 사용. 리스트는 0부터 시작하니까 1 더해준다.

