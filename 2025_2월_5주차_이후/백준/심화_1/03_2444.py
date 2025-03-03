# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

"""
입력 : 5
출력 : 
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""


'''풀이 과정 
입력값이 z = 5 일 때
               ' ' = x      * = y
    *       = (' ' * 4) + ('*' * 1)
   ***      = (' ' * 3) + ('*' * 3)
  *****     = (' ' * 2) + ('*' * 5)
 *******    = (' ' * 1) + ('*' * 7) 
*********   = (' ' * 0) + ('*' * 9) 
 *******    = (' ' * 1) + ('*' * 7) 
  *****     = (' ' * 2) + ('*' * 5)
   ***      = (' ' * 3) + ('*' * 3)
    *       = (' ' * 4) + ('*' * 1)

x = 1씩 작아졌다가  0 찍고 1 씩 커짐
y = 2 씩 커졌다가 x가 0 찍고 2 씩 작아짐

입력 값 z = 6 일 때
               ' ' = x      * = y
     *      = (' ' * 5) + ('*' * 1)
    ***     = (' ' * 4) + ('*' * 3)
   *****    = (' ' * 3) + ('*' * 5)
  *******   = (' ' * 2) + ('*' * 7)
 *********  = (' ' * 1) + ('*' * 9)
*********** = (' ' * 0) + ('*' * 11)
 *********  = (' ' * 1) + ('*' * 9)
  *******   = (' ' * 2) + ('*' * 7)
   *****    = (' ' * 3) + ('*' * 5)
    ***     = (' ' * 4) + ('*' * 3)
     *      = (' ' * 5) + ('*' * 1)
'''

''' 정답 1
answer_star = int(input())
space_count = []
star_count = []
x = ' '  
y = '*'

for i in range(1, answer_star + 1):        # 공백 개수 표 만들기
    space_count += [answer_star - i]       # answer_star = 5 >>> [4, 3, 2, 1, 0]

for q in range(1, answer_star + 1):        # 별 개수 표 만들기
    star_count += [2 * q - 1]              # answer_star = 5 >>> [1, 3, 5, 7 ,9]

star_count.reverse()                       # answer_star = 5 >>> [9, 7, 5, 3, 1]

for j in space_count:                      # 공백/별 모양 만들기
    space = x * j
    star = y * star_count[j]
    print(space + star)


space_count.reverse()                      # answer_star = 5 >>> [0, 1, 2, 3, 4]

for k in space_count:                      # 역순으로 만들기
    if k != 0:
        space = x * k
        star = y * star_count[k]
        print(space + star)
'''

# 다음엔 이렇게 풀어보자

"""정답 2(print문에 곱셈 사용으로 문제 해결)
N = int(input())

for i in range(1, N + 1):                       # 위쪽 삼각형 출력
    print(" " * (N - i) + "*" * (2 * i - 1))

for i in range(N - 1, 0, -1):                   # 아래쪽 삼각형 출력
    print(" " * (N - i) + "*" * (2 * i - 1))
"""


"""정답 3(가장 이상적인 문제 해결 방법)"""
answer_star = int(input())
x = ' '  
y = '*'

for i in range(1, answer_star + 1):             # 위쪽 삼각형 출력
    space = x * (answer_star - i)
    star = y * (2 * i - 1)
    print(space + star)

for i in range(answer_star - 1, 0, -1):         # 아래쪽 삼각형 출력
    space = x * (answer_star - i)
    star = y * (2 * i - 1)
    print(space + star)
