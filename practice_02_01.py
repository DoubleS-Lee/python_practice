# 파이썬으로 배우는 알고리즘 트레이딩
# https://wikidocs.net/2843

#%%
# 2-1
daum_price = 89000
naver_price = 751000

daum = 100
naver = 20

total = daum_price * daum + naver_price * naver

print(total)

# 2-2
daum_per = 0.05
naver_per = 0.1

total = daum_price * daum * daum_per + naver_price * naver * naver_per
print(total)

#%%
# 2-3
F=50
C = (F-32)/1.8

#%%
# 2-4
print('pizza\n'*10)

#%%
# 2-5
naver = 1000000
days = 3
for i in range(days):
    naver *= 0.7
print(naver)

#%%
# 2-6
print("이름: 파이썬 생년월일: 2014년 12월 12일 주민등록번호: 20141212-1623210")

#%%
# 2-7
s = 'Daum KaKao'
s = s[-5:] + " " + s[:4]
print(s)

#%%
# 2-8
a = 'hello world'
a = 'hi' + ' ' + a[-5:]
print(a)

#%%
# 2-9
x = 'abcdef'
x = x[1:5] + x[-1] + x[0]
print(x)

#%%
# 3-1
naver_closing_price = [474500, 461500, 501000, 500500, 488500]

# 3-2
print(max(naver_closing_price))

# 3-3
print(min(naver_closing_price))

# 3-4
print(max(naver_closing_price)-min(naver_closing_price))

# 3-5
print(naver_closing_price[2])

# 3-6
naver_closing_price1 = ['09/07','09/08','09/09','09/10','09/11']
naver_closing_price2 = dict(zip(naver_closing_price1,naver_closing_price))
print(naver_closing_price2)

# 3-7
naver_closing_price2['09/09']

#%%
# 4-1
for i in range(5):
    print('*',end='')
#%%
# 4-2
for i in range(4):
    for k in range(5):
        print('*', end='')
    print('')
    
#%%
# 4-3
for i in range(6):
    print('*'*i)

#%%
# 4-4
for i in range(6):
    print('*'*(5-i))
    
#%%
# ! 4-5 for문을 가지고 만들면 된다

#%%
# 4-9
apart = [[101, 102, 103, 104],[201, 202, 203, 204],[301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

for i in apart:
    for k in i:
        if k not in arrears:
            print(k)

#%%
# 5-1
def myaverage(a, b):
    result = (a+b)/2
    return result

print(myaverage(3,4))

#%%
# 5-2
def get_max_min(data_list):
    data_max = max(data_list)
    data_min = min(data_list)
    return data_max, data_min
a = [5,6,7,8,9,10]
print(get_max_min(a))

#%%
# ! 5-3 os.listdir(path) : path 디렉토리에 있는 모든 파일들을 보여준다
import os
def get_txt_list(path):

get_txt_list('c:/')


#%%
# 5-4
def bmi_func(weight, height):
    bmi = float(weight)/((float(height)*0.01)*(float(height)*0.01))
    print(bmi)
    if bmi < 18.5:
        result = '마른체형'
    elif 18.5 <= bmi < 25.0:
        result = '표준'
    elif 25.0 <= bmi < 30.0:
        result = '비만'
    else:
        result = '고도비만'
    return print(result)



weight = input('몸무게를 입력하세요 (kg) : ')
height = input('키를 입력하세요 (cm) : ')

print(bmi_func(weight, height))

#%%
# 5-6
def get_triangle_area(width, height):
    area = width * height * 0.5
    return print(area)

get_triangle_area(3,3)

#%%
# 5-7
def add_start_to_end(start, end):
    list_num = range(int(start),int(end)+1)
    return sum(list_num)

a = input('시작값을 입력하세요 : ')
b = input('마지막 값을 입력하세요 : ')
c = add_start_to_end(a,b)
print(c)

#%%
# 5-8
def string_3(list_str):
    list_after = []
    for i in list_str:
        list_after.append(i[:3])
    return list_after

list_str = ['Seoul', 'Daegu', 'Kwangju', 'Jeju']
k = string_3(list_str)
print(k)


#%%
# 6-1
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def setx(self,x):
        self.x = x
        return self.x
    
    def sety(self,y):
        self.y = y
        return self.y

    def get(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        return self.x, self.y
    
# 6-2
a = point(1,2)
print(a.setx(3))
print(a.sety(3))
print(a.get())
print(a.move(1,2))

#%%
# 6-3
class Stock():
    market = 'kospi'


a = Stock()
b = Stock()







































