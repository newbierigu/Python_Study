# 숫자 야구 게임을 한 단계씩 완성해 나갑시다. 
# 먼저 정답 숫자 3개를 뽑아 주는 generate_numbers() 함수를 작성할 것입니다. 
# 이 함수는 무작위로 0과 9 사이의 서로 다른 숫자 3개를 뽑고, 그 숫자들이 담긴 리스트를 리턴합니다.


from random import randint

def generate_numbers():
    numbers = []
    
    while len(numbers) < 3:
        picked_num = randint(0,9)
        
        if picked_num not in numbers:
            numbers.append(picked_num)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

print(generate_numbers())