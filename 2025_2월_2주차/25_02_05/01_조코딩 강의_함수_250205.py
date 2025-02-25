# 함수
# 똑같은 기능을 반복해서 사용해야 할 때 함수로 묶어서 한번에 사용할 때 사용
# 같은 기능끼리 정리하여 관리해서 보기 편함

# 파이썬 함수의 기본 구조
'''
def 함수 이름(매개변수):
     수행할_문장_1
     수행할_문장_2
'''

def add(a, b):          # 이 이름으로 사용할 거라고 함수를 만들고  (a, b = 매개변수)
    return a + b        # 이렇게 사용할 거라고 공식을 만든 후

print(add(1, 2))        # 정해논 이름처럼 형식을 맟춰서 사용하면 (1, 2 = 인수)
# 3                     # 정해놓은 공식을 사용하여 값이 나옴


####################################################################################

# 일반적인 함수
def add(a, b):
    return a + b

a = add(1, 2)
print(a)
#3


# 입력값이 없는 함수
def say():
    return 'Hi'

a = say()
print(a)
# Hi                                  # 입력값이 없어도 리턴값에 Hi 가 출력되도록 설정된 함수여서 결과는 Hi 가 출력력


# 리턴 값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d 입니다." %(a, b, a + b))

a = add(3, 2)
print(a)
# 3, 2의 합은 5 입니다.           # 함수 내 펑션에 프린트 값이 존재하여 해당 값이 출력 됨
# None                           # 리턴 값이 없으므로 변수 a에 리턴 값으로 들어가는 값은 없음 결과는 None
# None을 없애고 싶으면, return a + b 를 하면 None 대신 3 이 나온다.(= 리턴 값을 만들어주면 된다.)



# 입력/리턴값이 없는 함수
def say():
    print('Hi')

a = say()
print(a)
# Hi                             # 입력값이 없어서 함수이름만 사용됨, 와중에 리턴 값은 없지만 펑션에 프린트 값이 존재하여 Hi가 출력 됨
# None                           # 리턴 값이 없어서 변수 a에 들어가는 값이 없음 결과는 None




# 매개변수를 지정하여 호출
def add(a, b):
    return a - b

a = add(b=3, a = 7)              # 지정하지 않으면 위치대로 대입되지만 이런식으로 매개변수에 값을 지정하여 대입이 가능함.
print(a)
# 4




# 입력값이 많을 때 사용되는 함수
# 기본 구조
'''
def 함수이름(*매개변수):           매 개변수 대신에 *매개변수 가 들어감감
    수행할_문장_1
'''

def add_many(*args):             # many = args 에 들어가는 값들을 더해주는 함수
    result = 0
    for i in args:               # args를 순서대로 i에 대입시켜서서
        result = result + i      # result(0) + i 하겠다.
    return result

print(add_many(1, 2, 3, 4, 5))
# 15




# 입력값을 여러 개 받는 것 과 한 개 만 받는 것 섞어서 사용 가능
def add_mul(choice, *args):                # 목적 : args 요소를 가지고 choice 라는 인수에 add 를 넣으면 더하기 mul을 넣으면 곱하기 동작하는 함수 제작
    if choice == "add":                    # choice 가 add 면
        result = 0                         # result 값은 0 부터 시작
        for i in args:                     # i 라는 변수에 args 를 순서대로 대입해서
            result = result + i            # result(0) 부터 차례대로 더해준다.
    elif choice == "mul":                  # 그리고 만약 choice 에 mul 이 들어가면
        result = 1                         # result 값은 1 부터 시작
        for i in args:                     # i 라는 변수에 args 를 순서대로 대입해서
            result = result * i            # result(1) 에 i를 차례대로 곱한다.
    return result                          # 위 값을 리턴한다.

print(add_mul("mul", 3, 4))                # result = 1 >>> 1 * 3 = 3 >>> 3 * 4 = 12
# 12
print(add_mul("add", 7, 9 ))                # result = 0 >>> 0 + 7 = 7 >>> 7 + 9 = 16
# 16


 
# 키워드 매개변수 - kwargs

def print_kwargs(**kwargs):         # ** < 별 2개를 사용하여 키워드 매개변수로 활용용
    print(kwargs)


print_kwargs(a = 1)                 # 입력 값에 Key : Value 형태로 넣으면
# {'a': 1}                          # 딕셔너리 형태로 출력된다.
print_kwargs(name = 'foo', age = 3) 
# {'name': 'foo', 'age': 3}


# 키워드 매개 변수 활용법
def sub(**kwargs):
    print(kwargs['a'])              # a 값 만 뽑고 싶을 때

sub(a = 2, b = 3)
# 2

def sub(**kwargs):
    print(kwargs['b'])              # b 값 만 뽑고 싶을 때

sub(a = 2, b = 3)
# 3






# 함수의 리턴 값은 언제나 하나이다.
def add_and_mul(a, b):
    return a + b
    return a * b             # 함수는 return 문을 만나면 함수를 빠져나와 종료됨, 위 a+b 리턴문을 먼저 만나서 해당 리턴 문은 무시 됨.

print(add_and_mul(3, 4))
# 7


# 이 방법을 활용한 return 사용 법

def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." % nick)

say_nick("가나다")
say_nick("마바사")
say_nick("바보")                # "바보" 단어가 함수 안에서 리턴문과 만나서 그 다음 펑션이 진행되지 않고 함수 종료됨
# 나의 별명은 가나다 입니다.
# 나의 별명은 마바사 입니다.



# 매개변수의 초깃값 설정
def say_myself(name, age, man = True):
    print("내 이름은 %s 이고, 나이는 %d 입니다." %(name, age))
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("김철수", 19, True)
# 내 이름은 김철수 이고, 나이는 19 입니다.
# 남자입니다.

say_myself("박응용", 32)                       # 초깃값에 man = True 값을 설정하여 안 적어도 실행 됨.
# 내 이름은 박응용 이고, 나이는 32 입니다.
# 남자입니다.

say_myself("박예림", 27, False)
# 내 이름은 박예림 이고, 나이는 27 입니다.
# 여자 입니다.



# 함수 안에서 지정한 변수의 효력 범위
a = 1                     # 전역 변수

def vartest(a):           #
    result = a + 1    #
    return result         # 지역 변수

print(a)                  # print로 출력 하는것은 전역 변수임
# 1                       # 함수는 함수만 실행되고 값은 출력되지 않음

# 함수 값을 원한다면,
print(vartest(a))         # 이렇게 함수 명과 인수 값(=> a = 1)을 넣어서 받을 수 있음
# 2

'''
def vartest(a):
    a = a + 1   # 함수 안에서 선언된 변수는 함수 안에서만 사용된다.

vartest(3)
print(a)        # print(a) 에서 사용된 변수 a 는 어디에서도 선언되지 않았기 때문에 오류 발생됨.
'''


# 함수 안에서 함수 밖의 변수를 변경하는 방법

# return 활용
a = 1                   # 전역 변수 a = 1 설정
def vartest(a):
    a = a + 1           # 지역 변수로 a 설정 후 a + 1 이 a 라고 설정함
    return a            # return 으로 a 값을 vartest 함수에 받음
a = vartest(a)          # a 가 vartest(3) 이라고 설정한 상태
print(a)                # 에서 a를 print 하면
# 2                     # 지역 변수의 값이 출력된다.

# global 활용
a = 1                   # 전역 변수 a = 1 을 설정함

def vartest():          # 매개변수는는 존재하지 않음음
    global a            # global 은 밖에 있는 전역 변수를 가져 온다는 코드
    a = a + 1           

vartest()               # vartest에 아무것도 대입하지 않음
print(a)                # print(a) 는 2가 된다.
# 2



# 햇갈릴 수 있는 개념

# Immutable (정수, 실수, 문자열, 튜플)(= 변형이 불가능한 값)
a = 1
def vartest(a):
    a = a + 1

vartest(a)                      # 함수를 사용해도
print(a)                        # 전역 변수를 끌고 옴
# 1

# mutable (리스트, 집합, 딕셔너리)(=변형 가능한 값)
b = [1, 2, 3]
def vartest2(b):
    b = b.append(4)             # 변형을 시켜 줌.

vartest2(b)
print(b)                        # 변형 가능한 리스트라서 4 가 추가 됨
# [1, 2, 3, 4]


# 쉽게 정리하자면 Immutable 자료형 들은 함수 안에서 변형을 준다고 해도 함수 밖 동일이름 변수에는 영향을 주지 않음
# mutable 자료형들은 함수 안에서 변형을 주면 함수 밖 동일이름 변수에 영향을 준다.  




# lamda 예약어 # 패션코딩
# 기본 구조
'''
함수_이름 = lamda 매개변수_1, 매개변수_2 : 매개변수를_활용한_표현식
'''
def add(a,b):
    return a + b

print(add(3, 4))
# 7


# 위 함수를 lamda 사용하여 변형 가능
add = lambda a, b : a + b
result = add(3, 4)

print(result)
#7


# lambda 활용할 때
# 함수를 사용할 땐 이름을 반드시 정해야 함, 하지만 lamda는 함수 이름을 안 정하고 사용 가능하다.
# 실무에도 자주 사용(=간단한 함수수)
a = [lambda a, b : a + b, lambda a, b : a * b]
# 리스트 형태로 만들어서 인덱스 넘버로 불러옴
print(a[0](3, 4))
# 7
print(a[1](3, 4))
# 12