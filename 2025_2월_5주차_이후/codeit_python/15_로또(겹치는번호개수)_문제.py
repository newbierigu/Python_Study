# 실습 설명
# count_matching_numbers() 함수를 작성하세요. 
# 이 함수는 참가자가 뽑은 6개의 번호 리스트와 당첨 번호 6개의 리스트 중 몇 개의 숫자가 일치하는지 알려 주는 함수입니다. 
# 파라미터로 리스트 numbers와 리스트 winning_numbers를 받고, 두 리스트 사이에 겹치는 번호 개수를 리턴합니다.

def count_matching_numbers(numbers, winning_numbers):
    matching_num = 0

    for i in range(len(numbers)):
        for j in range(len(winning_numbers)):

            if numbers[i] == winning_numbers[j]:
                matching_num += 1

    
    return matching_num


# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))