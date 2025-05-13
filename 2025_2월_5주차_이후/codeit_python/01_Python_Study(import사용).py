# 만들어논 claculator 사용

from calculator import add, multiply

print(add(3, 4))
print(multiply(3, 4))


# stadard library 불러오기
# 1. math
import math

print(math.log10(100)) # 로그
print(math.cos(0)) # 코싸인
print(math.pi) # 원주율

# 2. random 
import random

print(random.random())          # .random() 함수는 0.0 과 1.0 사이의 랜덤한 수가 리턴됨
print(random.randint(1, 20))    # .randint() 함수는 a ≤ N ≤ b를 만족하는 어떤 랜덤한 정수 N을 리턴
print(random.uniform(0, 1))     # .uniform() 함수는 두 수 사이의 랜덤한 소수를 리턴하는 함수 

# os
import os                       # 파이썬으로 운영체제를 조작하기위해 사용

print(os.getlogin())            # 어떤 계정으로 로그인 되어있는지 확인
print(os.getcwd())              # 현재 사용중인 파일 경로 확인


# datetime '날짜'와 '시간'을 다루기 위한 다양한 '클래스'를 갗추고 있음.
import datetime
# 2020년 3월 14일을 파이썬으로 표현하기.
pi_day = datetime.datetime(2020, 3, 14)
print(pi_day)                   # 해당 코드 결과 2020-03-14 00:00:00 이다
print(type(pi_day))

# 시간 설정도 해보자.
pi_day = datetime.datetime(2020, 3, 4, 13, 6, 15)
print(pi_day)                   # 해당 코드 결과 2020-03-14 13:06:15 이다
print(type(pi_day))

# 오늘 날짜/시간을 받아와보자.
today = datetime.datetime.now()
print(today)
print(type(today))              # 현재 공부 중인 시간이 나온다. 2025-03-24 12:31:44.676101


# 두 시간 값 사이의 값을 얻고 싶을 때
today = datetime.datetime.now()
pi_day = datetime.datetime(2020, 3, 14, 13, 6, 15)
print(today - pi_day)
print(type(today - pi_day))     # <class 'datetime.timedelta'> datetime 값을 빼면, timedelta라는 타입이 나옴
                                # 날짜 간의 차이를 나타내는 타입

# timedelta를 생성해서 datetime에 더할 수 있음.
today = datetime.datetime.now()
my_timedelta = datetime.timedelta(days=10, hours=3, minutes=10, seconds=50) # 10일 3시간 10분 50초 후 시간

print(today)
print(today + my_timedelta)

# datetime 값에서 '연도'나 '월' 같은 값들을 추출
today = datetime.datetime.now()

print(today)
print(today.year)        # 연도
print(today.month)       # 월
print(today.day)         # 일
print(today.hour)        # 시
print(today.minute)      # 분
print(today.second)      # 초
print(today.microsecond) # 마이크로초


# datetime 값을 출력하면 별로 예쁘지 않음. 하지만 strftime() 함수를 사용하면, 우리 입맛대로 바꿀 수 있음.
today = datetime.datetime.now()

print(today)
print(today.strftime("%A, %B %dth %Y"))