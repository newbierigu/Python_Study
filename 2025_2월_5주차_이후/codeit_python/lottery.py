from random import randint


def generate_numbers(n):                                                            # 번호 뽑기
    picked_num = []
    count = 0

    while count < n:
        x = randint(1, 45)
        
        if x not in picked_num:
            picked_num.append(x)
            count += 1

    return picked_num



def draw_winning_numbers():                                                         # 당첨 번호 뽑기

    numbers = sorted(generate_numbers(6))

    while True:
        bonus_num = randint(1, 45)
        if bonus_num not in numbers:
            break
    
    return numbers + [bonus_num]




def count_matching_numbers(numbers, winning_numbers):                               # 겹치는 번호 확인
    matching_num = 0

    for i in range(len(numbers)):
        for j in range(len(winning_numbers)):

            if numbers[i] == winning_numbers[j]:
                matching_num += 1

    
    return matching_num




def check(numbers, winning_numbers):                                                # 당첨금 확인
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