# 실습 설명
# draw_winning_numbers() 함수를 작성하세요. 
# 이 함수는 일반 당첨 번호 6개와 보너스 번호 1개가 포함된 리스트를 리턴합니다. 
# 일반 당첨 번호 6개는 정렬되어 있어야 하고, 보너스 번호는 마지막에 추가하면 됩니다. 
# 앞서 정의한 generate_numbers() 함수를 잘 활용하면, 함수를 간결하게 작성할 수 있습니다.

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


def draw_winning_numbers():

    numbers = sorted(generate_numbers(6))         # 랜덤 번호 6개 뽑기

    while True:
        bonus_num = randint(1, 45)                # 새로운 랜덤 번호 1개 뽑기
        if bonus_num not in numbers:              # 중복되지 않으면 반복문 종료
            break
    
    return numbers + [bonus_num]

# 테스트 코드
print(draw_winning_numbers())



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


def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


# 테스트 코드
print(draw_winning_numbers())
"""