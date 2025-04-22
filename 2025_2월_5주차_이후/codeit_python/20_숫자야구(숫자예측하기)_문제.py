# 이번에는 유저에게 숫자 3개를 입력 받는 take_guess() 함수를 작성하겠습니다. 
# 이 함수는 유저에게 숫자 3개를 반복적으로 입력 받은 후, 유저가 입력한 숫자들을 리스트에 정리해서 리턴합니다. 
# 유저가 범위에서 벗어나는 숫자를 입력하면, 범위를 벗어나는 숫자입니다. 다시 입력하세요.라는 메시지가 출력되고 
# 마찬가지로 유저가 이미 입력한 숫자를 다시 입력하면, 중복되는 숫자입니다. 다시 입력하세요.라는 메시지가 출력됩니다.

# take_guess() 함수는 결과적으로 리스트를 리턴해야 합니다. 기억해 주세요!

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    guess_count = 1

    while guess_count <= 3:
        num = int(input(f"{guess_count}번째 숫자를 입력하세요: "))
        
        if not(0 <= num < 10):                                      # 0 이상 10 미만 숫자 거르기
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue

        elif num in new_guess:                                      # 중복되는 숫자 거르기
            print("중복되는 숫자입니다. 다시 입력하세요.")
            continue

        new_guess.append(num)                                       # 거름망 빠져나온 숫자 추가시키기
        guess_count += 1                                            # count 증가

    return new_guess
    
    
# 테스트 코드
print(take_guess())



