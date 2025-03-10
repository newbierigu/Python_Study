# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.



num_list = []                                   # 입력된 정수들을 리스트화해서 뽑기 위한 리스트 변수 생성
for _ in range(9):                              # 세로 줄로 입력되야하기에 for 반복문 생성
    num = int(input())                          # num = 임의의 입력된 정수
    num_list.append(num)                        # num_list에 입력된 정수 추가

num2 = max(num_list)                            # num2 = num_list내 최대 값
print(num2)                                     # num2 출력
print(num_list.index(num2) + 1)                 # num2의 위치 출력 (+ 1 은 인덱스자리로 0 부터 시작하기에 보기 좋게 + 1로 맟춰 줌)


'''
풀이과정에서의 오답

1. 25줄 : print(num2.index(max) + 1) 으로 하면
num2 는 이미 num_list 내의 최대 값이므로 리스트가 아니니 index가 오류가 발생함함

2. 25줄 : print(num_list.index(max) + 1) 으로 하면
max 는 내장 함수이기 때문에 index는 max를 리스트 요소로 찾으려 하기 때문에 오류가 발생함
max(num_list) or num2 로 했어야 함.
'''

