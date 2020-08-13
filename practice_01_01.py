# 초보자를 위한 파이썬 300제
# https://wikidocs.net/7014

# 1
print('Hello World')

# 2
print("Mary's cosmetics")

# 3
print('신씨가 소리질렀다. "도둑이야".')

# 4
print("c:\Windows")

# 5
print("안녕하세요.\n만나서\t\t반갑습니다.")

# 6
print("오늘은", "일요일")

# ! 7


# 8
print('naver','kakao','sk','samsung',sep='/')

# ! 9
print("first",end='');print("second")

# 10
print(5/3)

# 11
삼성전자 = 50000
보유주 = 10
총평가금액 = 삼성전자 * 보유주
print(총평가금액)

# 12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

# 13
s="hello"
t='python'

print(f'{s}! {t}')

# 14
2+2*3

# 15
a='128'
type(a)

# 16
num_str = "720"
int(num_str)

# 17
num=100
type(str(num))

# 18
a = '15.79'
type(float(a))

# 19
year = "2020"
year = int(year)
print(f"{year - 3} {year - 2} {year - 1}")

# 20
air_price = 48584
month = 36
total_price = air_price * month
print(total_price)

# 21
letters = 'python'
print(letters[0], letters[2])

# 22
license_plate = "24가 2210"
print(license_plate[-4:])

# ! 23
string = "홀짝홀짝홀짝"
print(f'{string[::2]}')

# !! 24
string = "PYTHON"


# ! 25
phone_number = "010-1111-2222"
print(f'{phone_number.replace("-"," ")}')

# 26
phone_number = phone_number.replace(" ","")
print(phone_number)

# ! 27
url = "http://sharebook.kr"
url = url.split('.')
print(f'{url[1]}')

# 28

# 29
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 30
# 31
# 32

# 33
print('-'*80)

# 34
t1 = 'python'
t2 = 'java'

print(f"{t1} {t2} "*4)

# 35, 36, 37
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print(f"이름 : {name1} 나이 : {age1}");print(f"이름 : {name2} 나이 : {age2}")

# ! 38
상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(',',''))


# ! 39
분기 = "2020/03(E) (IFRS연결)"
print(f'{분기[0:7]}')


# 40
data = "   삼성전자    "
data = data.strip()
print(data)

# 41
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 42
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 43
a='hello'
a=a.capitalize()
print(a)

# ! 44, 45
file_name = "보고서.xlsx"

# ! 46
file_name = "2020_보고서.xlsx"
file_name.startswith('2020')

# 47
a='hello world'
a.split()

# 48
ticker = "btc_krw"
ticker.split("_")

# 49
date = "2020-05-01"
date.split("-")

# 50
data = "039490     "
data.rstrip()

# 51
movie_rank = ['닥터스트레인지','스플릿', '럭키']

# 52
movie_rank.append('배트맨')

# ! 53
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,'슈퍼맨')

# ! 54
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
del movie_rank[3]

# ! 55
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2]
del movie_rank[2]


# 56
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1+lang2


# 57
nums = [1, 2, 3, 4, 5, 6, 7]
max_num = max(nums)
min_num = min(nums)

print(f'max : {max_num}\nmin : {min_num}')

# 58
nums = [1, 2, 3, 4, 5]
sum(nums)

# 59
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
len(cook)

# ! 60
nums = [1, 2, 3, 4, 5]
average = sum(nums)/len(nums)

# 61
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 62
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 63
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

# 64
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# ! 65
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[::2])


# !! 66
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']


# !! 67
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']


# !! 68
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']


# 69
string = "삼성전자/LG전자/Naver"
interest = string.split("/")

# ! 70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()


# 71
my_variable = ()

# 72
movie_rank = ("닥터 스트레인지","스플릿", "럭키")

# ! 73
a=(1, )

# 74

# !! 75

# ! 76
t = ('a', 'b', 'c')
t = ('A', 'B', 'C')


# ! 77
interest = ('삼성전자', 'LG전자', 'SK Hynix')
list(interest)


# 78
interest = ['삼성전자', 'LG전자', 'SK Hynix']
tutu = tuple(interest)

# 79

# 80
a = tuple(range(2,99,2))

# 81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,b,c=scores

# 82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score = scores

# 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, *valid_score, c = scores

# 84
temp = {}

# 85
a = {"메로나":1000, "폴라포":1200, "빵빠레":1800}

# !! 86


# 87
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print(f"메로나 가격 : {ice['메로나']}")

# 88
ice["메로나"] = 1300

# 89
del ice["메로나"]

# 90

# ! 91
inventory = {'메로나':[300,20], '비비빅':[400,3], '죠스바':[250,100]}

# !! 92
inventory = {"메로나":[300,20], "비비빅":[400,3], "죠스바":[250,100]}

# !! 93

# 94
inventory["월드콘"]=[500,7]

# ! 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream.keys()

# 95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
v = list(icecream.keys())

# 96
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
v = list(icecream.values())

# 97
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
s = sum(icecream.values())

# ! 98
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)


# !! 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)


# !! 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

































