# ★★ f 문자열 포매팅 (거의 포매팅은 이것만 사용함)
# 파이썬 3.6 버전 부터 f 문자열 포매팅 기능을 사용할 수 있다. 3.6 미만에선 사용 불가
print("★" * 100)
print("★왕 중요★ f 문자열 포매팅!")
print("name = '홍길동'")
print("age = 30")
print("print(f'나의 이름은 {name}입니다. 나이는 {age} 입니다.)")
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')


print("=" * 30)


# 제일 최신 버전의 포매팅 이므로 이것만 사용하면 된다. 중괄호 안 연산도 가능하다.
print("a = f'나이는 {age + 1}입니다.'")
print("print(a)")
a = f'나이는 {age + 1}입니다.'
print(a)


print("=" * 30)


# 좌/우/가운데 정렬도 f 포매팅으로 가능
# f''{"hi":<10}'
# f''{"hi":>10}'
# f''{"hi":^10}'

# 소수점 표시 많이 사용됨
print('y = 3.4123421')
print("a = f'{y:0.4f}'") 
print('print(a)')
y = 3.4123421
a = f'{y:0.4f}' # y값 안 소수를 4번째 까지 표시 하겠다.
print(a)


print("★" * 100)
print(

)

# 매소드

# 문자열 개수 세기 - count
# 문법은 .count('개수 셀 값')
a = "hobby"
print(a.count('b'))
# 2


print('=' * 30)


# 위치 알려주기 - find
# 문법은 .find('위치 찾을 값')
a = "hobby"
print(a.find('b')) #find 매소드 사용하여 'b' 의 위치 찾기
# 2 인덱스 개념으로 찾아줌 처음 나오는 b 의 위치가 [2] 니까 값은은 2 만약 없는 값을 찾아달라고 입력하면 '-1' 이 표시 됨
print(a.find('x'))


print('=' * 30)


# 위치 알려주기 2 - index
# 문법은 .index('위치 찾을 값')
a = "hobby"
print(a.index('h')) # index 매소드를 사용하여 h 의 위치 찾기
# 0 인덱스 개념으로 'h' 의 위치는 [0]
# a.find("x") 입력 시 find 와 다르게 오류 발생.')


print("=" * 30)


# 문자열 삽입 - join
# 문법 :  "x 사이에 넣을 값".join('x')
a = ", ".join('abcd') # ", " <<< 이걸 'abcd' 사이사이에 삽입 하겠단 뜻
print(a)
# a, b, c, d ", " 가 abcd 사이에 들어감


print("=" * 10)


# 문자열도 쓰지만 리스트에도 사용
a = ['a', 'b', 'c', 'd']
print(a)

a = " to the ".join(['a', 'b', 'c', 'd'])
print(a)


print('=' * 30)


# 대문자로 변경  - upper
# 문법 : x.upper()
a = "hi"
print(a.upper())
# HI


print('=' * 30)


# 소문자로 변경 - lower
# 문법 : x.lower()
a = "Hello World"
print(a.lower())
# "hello world"


print('=' * 30)


# 좌/우/양쪽 공백 지우기
# 문법 x.lstrip()/x.rstrip()/x.strip()
a = "      hi      "
print(a.lstrip()) # 왼쪽 공백 지우기
# hi
print(a.rstrip()) # 오른쪽 공백 지우기
#          hi
print(a.strip())  # 양쪽 공백 지우기
# hi


print("=" * 30)


# 문자 바꾸기 - replace >> 근데 이거 vscode에서 ctrl f 해서 바꿀 수 있음 똑같은 기능 
# 문법 : x.replace('변경될 문장', '변경할 문자')
a = "Life is too short"
print(a.replace("Life", "Your leg"))
# Your leg is too short

print("=" * 30)

# 문자열 나누기 - split
# 문법 : x.split(기준(공백은 띄어쓰기 기준))
a = "Life is too short"
print(a.split())
# ['Life', 'is', 'too', short] >>> 띄어쓰기 기준으로 나누어 리스트 형태로 값 출력


print("=" * 10)


# 만약 띄어쓰기가 없는 문자열을 split을 사용해 나눈다면
a = 'a:b:c:d'
print(a.split(':')) # .split('기준')을 사용하면 된다.
