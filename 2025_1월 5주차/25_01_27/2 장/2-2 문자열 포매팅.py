# 문자열 포매팅

"""
'현재 온도는 18도입니다.'
'현재 온도는 19도입니다.'
'현재 온도는 20도입니다.'
문장 안 숫자만 바꾸고 싶을 때
"""

eat = "I eat %d apples." %5
print(eat)
# I eat 5 apples.

number = 10
day = "three"
eat2 = "I ate %d apples. so I was sick for %s days." % (number, day)
print(eat2)
# I ate 10 apples. so I was sick for three days.

'''
문자열 포맷 코드
%s : 문자열(String)
%d : 정수(int)
%f : 부동 소수
%% : %를 문자 그대로 표시할 때
%o : 8진수 (자주 안씀)
%c : 문자 1개 (자주 안씀)
%x : 16진수 (자주 안씀)
'''
print('=' * 100)

# 포맷 코드와 숫자 함께 사용하기(지적허영심채우는용=별로 안중요)
e = "%10s" % "hi" # 전체 10칸 중에 'hi'라는 글자를 왼쪽에 두겠다.
print(e)

# 소수점은 좀 씀
print('소수점 포맷코드 : "%.f" 를 활용, 3.4123421 이란 소수에서 소수점 네 번째 자리 수 까지 가져올 땐 "f = "%0.4f" % 3.4123421" 을 사용함')
f = "%0.4f" % 3.4123421 # 소수점 4 번째 자리까지 가져오겠다는 뜻 (앞에 '0'은 위와 같이 칸 수 0은 상관 안하겠다는 뜻)
print(f)


print('=' * 100)


#.format 사용하기
print('.format 사용하기')
print('.format 사용하려면, {순서}가 들어간 문장이 있어야 된다.')
print('r = "I eat {0} apples.".format("five")')
r = "I eat {0} apples.".format("five") 
print("print(r)")
print(r)
# "I eat five apples."


print("=" * 30)



print('.format(5) : 정수가 들어가도 표시 됨')
print('h = "I eat {0} apples.".format(5)')
h = "I eat {0} apples.".format(5)
print("print(h)")
print(h)
# I eat 5 apples.


print("=" * 30)


# 2개 이상의 값을 넣는 것도 가능하다.
print('2개 이상의 값을 넣을 땐, {0}, {1} 로 순서를 정하고 .format(0에 들어갈 값, 1에 들어갈 값) 으로 설정한다.')
print('j = "I ate {0} apples. so I was sick for {1} days.".format(10, "three")')
j = "I ate {0} apples. so I was sick for {1} days.".format(10, "three") 
# {0}, {1}은 format 에 인덱싱 순서로 보면 된다. 그래서 바꿔서 쓸 수 도 있다 {1}, {0} 순으로 사용하면 사과 3개를 먹고 10일 아팠다. 란 표현이 된다.
# {0}, {1} 대신 변수 지정(.format(number = 10, day = "three")을 하여 {number}, {day}로도 사용 가능하다.) 
print("print(j)")
print(j)
# I ate 10 apples. so I was sick for three days.


print("=" * 100)


# 왼쪽 정렬 (자주 쓰이지 않음.)
print('왼쪽 정렬(개발할 때 자주 쓰이진 않음)')
print('c = "{0:<10}".format("hi")')
c = "{0:<10}".format("hi")
print('print(c)')
print(c)


print("=" * 30)


print('오른쪽 정렬(개발할 때 자주 쓰이진 않음)')
print('d= "{0:>10}".format("hi")')
d = "{0:>10}".format("hi")
print('print(d)')
print(d)


print("=" * 30)


print('가운데 정렬(개발할 때 자주 쓰이진 않음)')
print('g = "{0:^10}".format("hi")')
g = "{0:^10}".format("hi")
print('print(g)')
print(g)


print("=" * 30)


print('공백 채우기(개발할 때 자주 쓰이진 않음)')
print('v = "{0:=^10}".format("hi") : hi 를 가운데에 넣고 나머지 칸 들은 "=" 로 채우겠다.')
v = "{0:=^10}".format("hi")
print('print(v)')
print(v)


print("=" * 100)


# 소수점 표시 (자주사용)
print('y = 3.4123421')
print('a = "{0:10.4f}".format(y) : {0:10.4f} 에서 "0" 은 format 에 "y"를 의미하고, 10 은 전체 칸 수, .4f는 소수점 4 자리 까지 표시하겠다는 뜻')
print('print(a)')
y = 3.4123421
a = "{0:10.4f}".format(y)
print(a)



