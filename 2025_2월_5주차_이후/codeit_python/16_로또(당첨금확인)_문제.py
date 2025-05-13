# 실습 설명
# main.py 파일의 check() 함수를 작성하세요. 참고로 당첨 액수는 아래 규칙에 따라 결정됩니다.

# 내가 뽑은 번호 6개와 일반 당첨 번호 6개 모두 일치: 10억 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치, 그리고 내 번호 1개와 보너스 번호 일치: 5천만 원
# 내가 뽑은 번호 5개와 일반 당첨 번호 5개 일치: 100만 원
# 내가 뽑은 번호 4개와 일반 당첨 번호 4개 일치: 5만 원
# 내가 뽑은 번호 3개와 일반 당첨 번호 3개 일치: 5천 원
# check() 함수는 참가자의 당첨 금액을 리턴합니다. 
# 파라미터로 참가자가 뽑은 번호가 담긴 리스트 numbers와 주최측에서 뽑은 번호가 담긴 리스트 winning_numbers를 받는데요. 
# numbers는 당연히 번호 6개를 담고 있고, winning_numbers는 보너스 번호까지 해서 7개를 담고 있겠죠?

def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0

    for i in range(len(numbers)):
        for j in range(len(winning_numbers)):

            if numbers[i] == winning_numbers[j]:
                matching_num += 1

    
    return matching_num


def check(numbers, winning_numbers):

    bonus_num = [winning_numbers[-1]]
    general_num = list(winning_numbers[:-1])
    price = 0

    if count_matching_numbers(numbers,general_num) == 3:
        price = 5000
    
    if count_matching_numbers(numbers, general_num) == 4:
        price = 50000

    if count_matching_numbers(numbers, general_num) == 5:
        price = 1000000
     
    if count_matching_numbers(numbers, general_num) == 5 and count_matching_numbers(numbers, bonus_num) == 1:
        price = 50000000

    if count_matching_numbers(numbers, general_num) == 6:
        price = 1000000000
    return price

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))



# 정답 2(최적화 된 코드)
'''
def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0
    for num in numbers:
        if num in winning_numbers:
            matching_num += 1
    return matching_num

def check(numbers, winning_numbers):
    bonus_num = winning_numbers[-1]
    general_num = winning_numbers[:-1]

    count = count_matching_numbers(numbers, general_num)

    if count == 6:
        return 1000000000
    elif count == 5 and bonus_num in numbers:
        return 50000000
    elif count == 5:
        return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))'
'''