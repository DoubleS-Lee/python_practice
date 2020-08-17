#코딩도장
#http://codingdojang.com/list/1?sort=recommend&sort_order=fw


#%%
# http://codingdojang.com/scode/350?answer_mode=hide
# 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다. 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

num_list = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        num_list.append(i)
print(sum(num_list))


#%%
# http://codingdojang.com/scode/365?answer_mode=hide

list_gen = []
list_all = list(range(5001))

for i in range(5001):
    if i < 10:
        k = i + i
        list_gen.append(k)
    elif 10 <= i < 100:
        i = str(i)
        k = int(i[0])+int(i[1])+int(i)
        list_gen.append(k)
        
    elif 100 <= i <1000:
        i = str(i)
        k = int(i[0])+int(i[1])+int(i[2])+int(i)
        list_gen.append(k)
    else:
        i = str(i)
        k = int(i[0])+int(i[1])+int(i[2])+int(i[3])+int(i)
        list_gen.append(k)

for i in list_gen:
    for k in list_all:
        if i == k:
            list_all.remove(k)

print(list_all)

sum(list_all)
#리스트를 만들어서 5000까지의 제네레이터를 만들고 이 값을 0~5000까지의 값들과 빼줘서 남는걸 고르면 그게 셀프 넘버들

#%%
# 리스트를 만드는 법
list_1 = [i for i in range(10)]

def plus_ten(input_val):
    return input_val + 10

list_1 = [plus_ten(i) for i in range(10)]

#
cnt_list = [0 for i in range(10)]

#%%
import numpy as np

score_list = np.random.randint(0, 20, size = (1000))

cnt_dict = dict()

for score in score_list:
    cnt_dict[score] = cnt_dict.get(score, 0) + 1

print(cnt_dict)

dir(cnt_dict)












