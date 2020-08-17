# 초보자를 위한 파이썬 300제
# https://wikidocs.net/7014

# 201
def print_coin():
    print('비트코인')

# !202
print_coin()

# 203
for a in range(100):
    print_coin()

# 204
def print_coins():
    for a in range(100):
        print_coin()
        
# 205~214
        
# 215
def print_with_smile(a):
    print(f'{a} :D')
    
# 216
print_with_smile('안녕하세요')    
    
# 217
def print_upper_price(num):
    print(num*1.3)

# 218
def print_sum(a, b):
    print(a+b)

# 219
def print_arithmetic_operation(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# 220
def print_max(a,b,c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    elif b > c:
        print(b)
    else:
        print(c)
#%%
# !221
def print_reverse(a):
    for i in a[::-1]:
        print(i)
    
print_reverse('python')

#%%
# !222 
def print_score(score):
    return sum(score)/len(score)
        
print(print_score([1,2,3]))

#%%
# 223
def print_even(a):
    for i in a:
        if i % 2 == 0:
            print(i)
    
print_even([1, 3, 2, 10, 12, 11, 15])
    
# 224
def print_keys(a):
    for i in a.keys():
        print(i)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

# 225
def print_value_by_key(dic,date):
    print(dic[date])
    
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")
#%%
# !!226
def print_5xn(a):
    num = int(len(a)/5)
    for i in range(num):
        print(a[i*5:i*5+5])
        
print_5xn("아이엠어보이유알어걸")


#%%
# !!227
def print_mxn(a,num):
    string_num = int(len(a)/num) + 1
    for i in range(string_num):
        print(a[i*num:i*num+num])

print_mxn("아이엠어보이유알어걸", 3)

#%%

# 228
def calc_monthly_salary(annual_salary):
    a = int(annual_salary/12)
    return a

calc_monthly_salary(12000000)

# 229~231

# 232
def make_url(a):
    return "www."+a+".com"

make_url("naver")

#233
def make_list(a):
    li = []
    for b in a:
        li.append(b)
    return li

make_list("abcd")

# 234
def pickup_even(a):
    my_list = []
    for i in a:
        if i % 2 == 0:
            my_list.append(i)
    return my_list


pickup_even([3, 4, 5, 6, 7, 8])

# 235
def convert_int(a):
    a = a.replace(",","")
    return int(a)

convert_int("1,234,567")

# 236~240

# !241

# 242
import datetime
type(datetime.datetime.now())

# !243~249

# 250
import numpy as np
a = np.arange(0,5.1,0.1)
print(a)

# 251
#클래스
#객체
#인스턴스

#%%
# !252~259
class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def who(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.sex}')
    
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print("나의 죽음을 알리지 말라")

areum = Human('아름', 25, '여자')
areum.who()
del areum



#%%
# !261~270
class Stock():
    def __init__(self, name, code, per, pbr, profit):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.profit = profit
    
    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
        
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_per(self,per):
        self.per = per
    
    def set_pbr(self,pbr):
        self.pbr = pbr
    
    def set_dividend(self,profit):
        self.profit = profit


a = Stock("삼성전자", "005930",15.79,1.33,2.83)
b = Stock("현대차", "005380",8.70,0.35,4.27)
c = Stock("LG전자", "066570",317.34,0.69,1.37)

s_list = [a,b,c]

for i in s_list:
    print(i.code, i.per)

삼성.set_per(12.75)
print(삼성.per)



#%%
# !! 271~280



#%%
# !! 281~290

























