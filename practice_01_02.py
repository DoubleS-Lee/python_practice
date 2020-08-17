# 초보자를 위한 파이썬 300제
# https://wikidocs.net/7014

# 101~110

# 111
a = input('입력: ')
print(a*2)

# 112
a = input('숫자를 입력하세요: ')
print(int(a)+10)

# 113
a = input('숫자를 입력하세요: ')
if int(a) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 114
a = input('입력값: ')
a = int(a)
if a > 255:
    print('출력값: 255')
else:
    print(f'출력값: {a+20}')

# 115
a = input('입력값 : ')
a = int(a)
num = a - 20
if num < 0:
    print("출력값 : 0")
elif num > 255:
    print("출력값 : 255")
else:
    print(f'출력값 : {num}')

# !! 116



# 117
fruit = ["사과", "포도", "홍시"]
a = input('좋아하는 과일은? : ')
if a in fruit:
    print('정답입니다')
else:
    print('오답입니다.')

# 118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
a = input("종목을 입력하세요 : ")
if a in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다')

# 119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input('제가 좋아하는 계절은 : ')
if a in fruit.keys():
    print('정답입니다')
else:
    print('오답입니다')

# 120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
a = input('제가 좋아하는 과일은 : ')
if a in fruit.values():
    print('정답입니다')
else:
    print('오답입니다')

# ! 121
a = input('문자 한개를 입력하세요 : ')
if a.isupper():
    print(a.lower())
else:
    print(a.upper())

# 122
a = input('점수를 입력하세요 : ')
a = int(a)
if 80<a<=100:
    print("graid is A")
elif 60<a<=80:
    print("graid is B")
elif 40<a<=60:
    print("graid is C")
elif 20<a<=40:
    print("graid is D")
elif 0<=a<=20:
    print("graid is E")

#%%
# !!! 123 if를 쓰지말고 dictionaly를 가지고 만들어보자
환율 = {'달러':1167, '엔':1.096, '유로':1268, '위안':171}




#%%
# ! 124
a = int(input('input number1 : '))
b = int(input('input number2 : '))
c = int(input('input number3 : '))
d = [a,b,c]
max(d)

# ! 125
number = input('휴대전화 번호 입력 : ')
info = {'011':'SKT', '016':'KT', '019':'LGU', '010':'알수없음'}
a = number[0:3]
if a == '011':
    print(f'당신은 {info[a]} 사용자입니다.')
elif a == '016':
    print(f'당신은 {info[a]} 사용자입니다.')
elif a == '019':
    print(f'당신은 {info[a]} 사용자입니다.')
elif a == '010':
    print(f'당신은 {info[a]} 사용자입니다.')
    
    
# 126
num = input("우편번호 : ")
a = int(num[2])
if a == 0 or a==1 or a==2:
    print('강북구')
elif a == 3 or a==4 or a == 5:
    print('도봉구')
elif a == 6 or a==7 or a == 8 or a == 9:
    print('노원구')

# ! 127
a = input('주민등록번호 : ')
if a[7] == '1' or a[7] == '3':
    print('남자')
elif a[7] == '2' or a[7] == '4':
    print('여자')


# 128
num = input("주민등록번호 : ")
num = num.split('-')[1]
if 0 <= int(num[1:3]) <=8:
    print('서울입니다')
else:
    print('서울이 아닙니다')

# 129
num = input('주민등록번호 : ')
num = num.replace('-','')
sum = 0
for i in range(0,8):
    a = int(num[i])*(i+2)
    sum = sum + a
for i in range(8,12):
    a = int(num[i])*(i-6)
    sum = sum + a
loss = sum % 11
if loss == 4:
    print('유효한 주민등록번호입니다')
else:
    print('유효하지 않은 주민등록번호입니다.')

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
num = int(btc['opening_price']) + int(btc['max_price']) - int(btc['min_price'])

if num > int(btc['max_price']):
    print('상승장')
else:
    print('하락장')

# 131~142
    
# 143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 회사 in 리스트:
    print(f'{len(회사)}')

# 144
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(f'{동물} {len(동물)}')

# 145
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(f'{동물[0]}')

# 146
리스트 = [1, 2, 3]
for a in 리스트:
    print(f'3 x {a}')

# 147
리스트 = [1, 2, 3]
for a in 리스트:
    print(f'3 x {a} = {a*3}')

########################################## 148
리스트 = ["가", "나", "다", "라"]  
for a in 리스트[1:]:
    print(a)

# !149
리스트 = ["가", "나", "다", "라"]  
for i in 리스트[::2]:
    print(i)

# 150
리스트 = ["가", "나", "다", "라"]  
for a in 리스트[::-1]:
    print(a)

# 151
리스트 = [3, -20, -3, 44]
for a in 리스트:
    if a < 0:
        print(a)

# 152
리스트 = [3, 100, 23, 44]
for a in 리스트:
    if a % 3 == 0:
        print(a)

# 153
리스트 = [13, 21, 12, 14, 30, 18]
for a in 리스트:
    if a < 20 and a % 3 == 0:
        print(a)

# 154
리스트 = ["I", "study", "python", "language", "!"]
for a in 리스트:
    if len(a) >= 3:
        print(a)

# 155
리스트 = ["A", "b", "c", "D"]
for a in 리스트:
    if a.isupper() == True:
        print(a)

# 156
리스트 = ["A", "b", "c", "D"]
for a in 리스트:
    if a.islower():
        print(a)

# 157
리스트 = ['dog', 'cat', 'parrot']
for a in 리스트:
    a = a.capitalize()
    print(a)

# 158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for a in 리스트:
    a = a.split('.')
    print(a[0])

# 159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for a in 리스트:
    b = a.split('.')
    if b[1] is 'h':
        print(a)

# 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for a in 리스트:
    b = a.split('.')
    if (b[1] is 'h') or (b[1] is 'c'):
        print(a)

# 161
for a in range(0,100):
    print(a)

# 162
for a in range(2002,2051,4):
    print(a)

# 163
for a in range(1,31):
    if a % 3 == 0:
        print(a)

# !! 164
for i in range(100):
    print(99-i)

# 165
for a in range(0,10):
    print(a/10)

# 166
for a in range(1,10):
    print(f'3x{a} = {a*3}')

# 167
for a in range(1,10):
    if a%2!=0:
        print(f'3x{a} = {a*3}')

# 168
sum = 0
for a in range(1,11):
    sum += a
print(sum)

# 169
sum = 0
for a in range(1,11):
    if a % 2 != 0:
        sum += a
print(sum)

# 170
sum = 1
for a in range(1,11):
    sum *= a
print(sum)

# 171
price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)):
    print(price_list[a])

# !! 172
price_list = [32100, 32150, 32000, 32500]
for i, price in enumerate(price_list):
    print(i,price)

# !173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(f'{len(price_list)-i} {price_list[i]}')

# 174
price_list = [32100, 32150, 32000, 32500]
for a in range(len(price_list)-1):
    print(f'{100+10*a} {price_list[a+1]}')

# 175
my_list = ["가", "나", "다", "라"]
for a in range(len(my_list)-1):
    print(f'{my_list[a]} {my_list[a+1]}')

# 176
my_list = ["가", "나", "다", "라", "마"]
for a in range(len(my_list)-2):
    print(f'{my_list[a]} {my_list[a+1]} {my_list[a+2]}')

# 177
my_list = ["가", "나", "다", "라"]
for a in range(len(my_list)-1):
    print(f'{my_list[3-a]} {my_list[2-a]}')

# 178
my_list = [100, 200, 400, 800]
for a in range(len(my_list)-1):
    print(f'{my_list[a+1] - my_list[a]}')

# 179
my_list = [100, 200, 400, 800, 1000, 1300]
for a in range(len(my_list)-2):
    sum = my_list[a]+my_list[a+1]+my_list[a+2]
    average = float(sum/3)
    print(f'{average}')

# 180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for a in range(len(low_prices)):
    vol = high_prices[a] - low_prices[a]
    volatility.append(vol)

# 181
apart = [['101호','102호'],['201호','202호'],['301호','302호']]

# 182
stock = [['시가',100,200,300],['종가',80,210,330]]

# 183
stock = {'시가':[100,200,300],'종가':[80,210,330]}

# 184
stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}

# !! 185
# range랑 len 쓰지말고 구현해보기
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for k in i:
        print(k)


# !!! 186
# range랑 len 쓰지말고 구현해보기
apart = [ [101, 102], [201, 202], [301, 302] ]



# 187
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart[::-1]:
    for b in a[::-1]:
        print(f'{b}호')

# 188
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(f'{b} 호')
        print('-------')

# 189
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(f'{b}호')
    print('-'*5)

# 190
apart = [ [101, 102], [201, 202], [301, 302] ]
for a in apart:
    for b in a:
        print(f'{b}호')
print('-'*5)

# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for a in data:
    for b in a:
        print(f'{b+b*0.00014}')

# 192
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for a in data:
    for b in a:
        print(f'{b+b*0.00014}')
    print('-'*5)

# 193
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for a in data:
    for b in a:
        b += b*0.00014
        result.append(b)
print(result)    

# 194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for a in data:
    re = []
    for b in a:
        b = b*1.00014
        re.append(b)
    result.append(re)
print(result)

# !195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:4]:
    print(i[3])


# 196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for a in ohlc[1:]:
    if a[3] > 150:
        print(a[3])

# 197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for a in ohlc[1:]:
    if a[3] >= a[0]:
        print(a[3])

# 198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for a in ohlc[1:]:
    volatility.append(a[1]-a[2])
print(volatility)

# 199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for a in ohlc[1:]:
    if a[3] > a[0]:
        print(a[1]-a[2])

# 200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
sum = 0
for a in ohlc[1:]:
    sum += a[3]-a[0]
print(sum)














































