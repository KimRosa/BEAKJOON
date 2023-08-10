# 단어공부


word = input().upper()
the_word = list(set(word))

cnt_list = []

for i in the_word:
    cnt = word.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")

else:
    max_index = cnt_list.index(max(cnt_list))
    print(the_word[max_index])
