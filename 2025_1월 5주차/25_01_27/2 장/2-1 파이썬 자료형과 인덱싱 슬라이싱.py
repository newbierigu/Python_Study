# 파이썬 자료형 배우기
# ex) 1 + 1 = 2(정수 일 때) // '1' + '1' = '11' (문자 일 때)
# 숫자, 문자열, 불, 변수, 리스트, 튜플, 딕셔너리, 집합 등이 있음

# ★ 변수 : 쉽게 이해해서 박스 값을 담는 개념, a = 3 의 뜻은 같다라는 뜻이 아니라 a에 3을 담는다는 개념

'''
숫자형
: ★ 정수형 (1, 2, -2) "int"
  ★ 실수형 (1.24, -34.56) "float"
  컴퓨터식 지수 표현 방식 (4.24e10, 4.24e-10)
  8진수 (0o37)
  16진수 (0x7A)
  '''

# 자료형 구분 언어
# type(a) >>> 자료형 구분 언어. a 가 123 이니 정수(int) 형으로 나옴. a = 1.23 였다면 '<class = 'float'>' 나옴
print("자료형 구분 언어'type(x)'")
x = 123
print(type(x))
# <class = 'int'>


print('=' * 100)



# 사칙 연산
print("사칙연산")
a = 3
b = 4
c = 7
print('a = 3')
print('b = 4')
print('c = 7')

print('더하기 : a + b')
print(a + b)
# 7
print('빼기 : a - b')
print(a - b)
# 1
print('곱하기 : a * b')
print(a * b)
# 12
print('나누기 : a / b')
print(a / b)
# 0.75
print('제곱 : a ** b a의 b 승')
print(a ** b)
# 81
print('"나머지" 의 연산자 : c % a')
print(c % a)
# 1


print('=' * 100)



'''
문자열 자료형
따옴표로 감싸면 "123", '234' 이건 정수가 아닌 문자형(str이 됨)
'''
print("자료형 구분 언어'type(y)'")
y = '123'
print(type(y))
# <class = 'str'>

# 큰/작은 따옴표로 감싸면 문자열이 됨 ex: '123' "123" '''안녕하세요''' """123"""
# \' < 이 기능은, 문자열에 ' < 이거 추가 가능
# 줄 바꿈 : \n 사용
print("Life\'s too short,\nYou need python.")
# Life 's too short
# You need python.


print('=' * 100)


'''
문자열 연산하기
'''

# 문자열과 정수 만 곱할 수 있음 문자열 문자열은 X
print('문자열 연산으로 head = "Python", tali = " is fun!" 을 더하면')
print('head + tail')
head = "Python"
tail = " is fun!"
print(head + tail)
print('"head" 만 3번 곱하면?')
print(head * 3)
# Python is fun!
# PythonPythonPython


print('=' * 50)
print("My Program")
print('=' * 50)
# ==================================================
# My Program
# ==================================================


print('=' * 100)


# 문자열 길이 구하기
print('a1 = "Life\'s too short." 의 문자열 길이를 구하는 함수 는 len(x)')
a1 = "Life\'s too short." # \' 가 한 글자
print(len(a1))
# 17


print('=' * 100)


# 인덱싱 과 슬라이싱 ★파이썬은 0 부터 시작한다★
# 인덱싱
a2 = "Life is too short, you need python."
print(a2[3])
# e
print(a2[0])
# L
print(a2[12])
# s
print(a2[-1])
# .


print('=' * 100)


# 슬라이싱 a2[ : : ] [이상 : 미만 : 간격] 개념으로 문자를 잘라서 표시
a2 = "Life is too short, you need python."
print(a2[ : 4])
# Life
print(a2[ : :-1]) # 처음부터 끝까지 한 칸 간격으로 모든 문자가 거꾸로 표시 됨
# .nohtyp deen uoy ,trohs oot si efiL
print(a2[ : :-2]) #  처음부터 끝까지 두 칸 간격으로 모든 문자가 거꾸로 표시됨.
# .otpde o tosots fL
print(a2[19: ])
# you need python.
print(a2[19:-8])
# you need


print('=' * 100)

