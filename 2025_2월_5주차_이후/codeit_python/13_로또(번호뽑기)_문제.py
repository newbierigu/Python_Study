# 실습 설명
# 로또 시뮬레이션 프로그램을 한 단계씩 완성해 나갑시다.

# 먼저 generate_numbers() 함수를 작성하세요. 
# 이 함수는 파라미터로 정수 n을 받습니다. 
# 무작위로 1과 45 사이의 서로 다른 번호 n개를 뽑고, 그 번호들이 담긴 리스트를 리턴합니다. 
# 참고로 이 함수는 참가자의 번호를 뽑는 데에도 쓰이고, 보너스를 포함한 당첨 번호 7개를 뽑는 데에도 쓰입니다.

from random import randint


def generate_numbers(n):
    picked_num = []                 # 리스트로 유지
    count = 0                       # 반복 횟수 확인

    while count < n:                # n보다 count 가 작을 때 반복
        x = randint(1, 45)          # x는 1~45중에서 랜던 값
        
        if x not in picked_num:     # x 가 num에 포함되어있지 않다면,
            picked_num.append(x)    # num에 x 추가
            count += 1              # count 횟수 증가

    return picked_num

print(generate_numbers(6))



# 정답 2

"""
from random import randint


def generate_numbers(n):
    numbers = []

    while len(numbers) < n:
        num = randint(1, 45)
        if num not in numbers:
            numbers.append(num)

    return numbers
"""