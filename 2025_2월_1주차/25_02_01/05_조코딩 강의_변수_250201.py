# 변수
# 변수는 아래와 같이 변수_이름 = 변수에_저장할_값 이라는 개념이다.
'''
a = 1        # '=' 은 assignment 이다.
b = 'python'
c = [1, 2, 3]
'''
# 그걸 조금 더 뜯어서 본다면, 
# a = [1, 2, 3] 이라고 한다면 [1, 2, 3] 값을 가지는 리스트 데이터(객체) 가 자동으로 메모리에 생성되고
# 변수 a는 [1, 2, 3] 리스트가 저장된 메모리의 주소인 셈이다.
# [1, 2, 3] == 객체
# a == 메모리 주소

# 객체의 메모리 주소 값을 리턴하는 함수 - id(변수)
a = [1, 2, 3]
print(id(a))
# 2572912009536    <<< 메모리 주소 (변수 a 의 조수 값값)


# 리스트를 복사하고자 할 때
 # 흔하게 혼동하는 사례
a = [1, 2, 3]
b = a

print(id(a))
print(id(b))
# 2773936726016
# 2773936726016

print(a is b)    # a is b 는 주소값이 같은지 직관적으로 알 수 있다.
# True



# 여기서 2 값을 4 로 변경했을 때
a = [1, 2, 3]     # a 주소에 [1, 2, 3] 리스트 데이터(객체) 를 저장한다.
b = a             # 변수 b 는 변수 a 와 같은 주소 값을 사용한다.
a[1] = 4          # 리스트[1] 위치를 4 로 변경한다.

print(a)          # 변경한 변수 a 값을 출력한다.
print(b)          # 변수 b 값을 출력한다.
# [1, 4, 3]
# [1, 4, 3]     <<<<  a 는 [1, 4, 3] 이 이해가는데 b 는 왜 바꼈나?

# 원리를 파보면 변수 b에는 a 의 주소 값을 담는것이다.
# 그러므로 변수 a 의 주소에 들어가있는 리스트 데이터(객체) 가 [1, 2, 3] 에서 [1, 4, 3] 으로 변경되었으므로
# 변수 b도 같은 주소 값을 사용하므로 해당 값을 리턴하게 된다.



# b 변수가 a 변수의 객체를 복사해도, a 변수의 주소 값을 복사하지 않는 방법

# [:] 리스트 전체를 가리키는 슬라이싱으로 복사하기
a = [1, 2, 3]
b = a[:]           # 리스트 전체를 가리키는 슬라이싱[:] 으로 객체를 복사함
a[1] = 4

print(a)
print(b)
# [1, 4, 3]
# [1, 2, 3]        # 이와 같이 [:] 로 복사 시 주소 값은 가져오지 않는다

print(a is b)
# False            # 주소가 같지 않다는 결과




# 모듈 copy 를 사용하는 방법 (리스트 내장 함수 copy와 다름) 복사하는 기능을 가진 모듈임.

from copy import copy    # 나중에 배울 copy 모듈
a = [1, 2, 3]
b = copy(a)
print(b)
# [1, 2, 3]        # a의 리스트를 복사함

print(a is b)
# False            # 주소가 같지 않다는 결과



# 리스트 함수 copy 도 사용 가능
# 위와 완전 동일함
a = [1, 2, 3]
b = a.copy()       # 리스트 함수 copy 로 a 의 리스트를 복사
print(b)

print(a is b)


# 변수의 활용 방법

# 튜플 활용 방법
a, b = ('python', 'life')
print(a)
print(b)
# python
# life


# 위와 완전 동일함
(a, b) = 'hello', 'world'
print(a)
print(b)
# hello
# world

# 리스트 활용 방법

[a, b] = ['a', 1, 2, 'b'], [3, 4, 'c', 5, 'd']
print(a)
print(b)
# ['a', 1, 2, 'b']
# [3, 4, 'c', 5, 'd']

[a, b] = ['python', 'good']
print(a)
print(b)
# python
# good

# 같은 값을 더 쉽게 넣는 법

a = b = 'python'
print(a)
print(b)
# python
# python

print(a is b)
# True




# 위 방법을 활용하여 변수들의 값 바꾸기 (파이썬만 가능)

a = 3
b = 5

a, b = b, a     # a 와 b 의 값을 바꿈
print(a)
print(b)
# 5
# 3