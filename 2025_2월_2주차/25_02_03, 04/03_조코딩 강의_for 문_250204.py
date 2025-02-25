# for 문
# for 문은 while 문과 비슷한 반복문이다.
# for 문은 리스트나 문자열이나 튜플이나 여러 개의 자료가 담긴 것을 하나씩 뽑아 쓸 때 사용하는 반복문이고
# while 문은 커피 예제같이 상황이이 주어주고 계속 반복해서 빠져나오거나 조건이 틀어졌을때 끝나게 끔 설정하는 반복문이다.

# for문의 기본 구조
'''
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장_1
    수행할_문장_2
'''
# for 문은 리스트(또는 튜플/문자열)의 첫 번째 요소 부터 마지막 요소 까지 변수에 대입하여 수행할 문장 1/2를 수행한다.


# for 문 기본 예시
test_list = ['one', 'two', 'three']
for i in test_list:                 # i 라는 변수에 test_list에 있는 요소 처음부터 하나씩 쪼개서 담겠다.
    print(i)
# one
# two
# three




# for 문의 다양한 활용
a = [(1, 2), (3, 4), (5, 6)]
for first, last in a:       # first/last 변수 창조 하여 a에서 순서대로 first last에 대입하여 반복 수행한다.
    print(first + last) 
# 3
# 7
# 11

a = [(1, 2), (3, 4), (5, 6)]
for first in a:       # first 라는 변수 창조 / 순서대로 튜플 하나씩 가져 옴
    print(first)
# (1, 2)
# (3, 4)
# (5, 6)

a = [(1, 2), (3, 4), (5, 6)]
for first, second in a:       # first와 second 라는 변수 창조 / 순서대로 요소 하나씩 가져 옴
    print(first)
    print(second)
# 1
# 2
# 3
# 4
# 5
# 6

# for 문의 실질적 활용

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:                              # mark 라는 변수 창조하여 marks 요소들을 순서대로 대입
    number += 1                                 # 학생들 번호 붙여줌
    if mark >= 60:                              # 대입된 변수를 해당 구문 순서대로 반복 수행
        print("%d번 학생 합격입니다." %number)
    else:
        print("%d번 학생 불학격 입니다." %number)
# 1번 학생 합격입니다.
# 2번 학생 불학격 입니다.
# 3번 학생 합격입니다.
# 4번 학생 불학격 입니다.
# 5번 학생 합격입니다.


# for 문과 continue 문

marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:                                       # mark 변수 창조하여 marks 요소 순서대로 대입
    number += 1                                         # 학생들 번호 순서대로 + 1 씩 부여
    if mark < 60:                                       # 만약 학생 점수가 60점 미만이면
        continue                                        # 처음으로 돌아가서 다시 실행하고고
    print("%d번 학생, 축하합니다. 합격입니다." %number)   # 60점 이상이면 해당 문구 출력력
# 1번 학생, 축하합니다. 합격입니다.
# 3번 학생, 축하합니다. 합격입니다.
# 5번 학생, 축하합니다. 합격입니다.



# for 문과 함께 자주 사용하는 함수 range 함수
# range는 범위를 나타낼 때 자주 사용함
add = 0
for i in range(1, 11):                 # range(이상, 미만) 범위 설정
    add += i                           # add + i 변수에 추가 반복복
    print(add)
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45
# 55

# 1 ~ 100 까지 더하는 함수수
add = 0
for i in range(1, 101):
    add += i
    print(add)


# 반복문 안에 반복문
for i in range(2, 10):             # 1번 for문
    for j in range(1, 10):         # 2번 for문
        print(i * j, end = " ")        # i x j 이후 end = " " << 띄어쓰기 용도
    print(' ')                      # 한 줄 넘기기 용도
# 2 4 6 8 10 12 14 16 18
# 3 6 9 12 15 18 21 24 27
# 4 8 12 16 20 24 28 32 36
# 5 10 15 20 25 30 35 40 45
# 6 12 18 24 30 36 42 48 54
# 7 14 21 28 35 42 49 56 63
# 8 16 24 32 40 48 56 64 72
# 9 18 27 36 45 54 63 72 81




# 리스트 컴프리헨션 사용하기 - 실전용 아님 # 패션 코딩

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)
print(result)

# 위 함수를 패션 코딩 하면

a = [1, 2, 3, 4]
result = [num * 3 for num in a]      # [표현식 for 변수 in 반복_가능_객체 if 조건문] 형식이다.

print(result)

# 이렇게 줄일 수 있다.

# [표현식 for 변수1 in 반복_가능_객체1 if 조건문1
#        for 변수2 in 반복_가능_객체2 if 조건문2
#        for 변수3 in 반복_가능_객체3 if 조건문3]

# 위 같이도 가능하다.

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]   # 짝수만 뽑아 쓰겠다.

print(result)

# 위 방식을 풀어쓰면

a = [1, 2, 3, 4]

result = []
for num in a:
    if num % 2 == 0:
        result.append(num * 3)

print(result)

# 이 된다.
