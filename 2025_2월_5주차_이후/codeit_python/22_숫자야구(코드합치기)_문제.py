from random import randint


def generate_numbers():
    numbers = []
    
    while len(numbers) < 3:
        picked_num = randint(0,9)
        
        if picked_num not in numbers:
            numbers.append(picked_num)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


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


def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        
        if guesses[i] == solution[i]:           # guesses 와 solution의 요소 값과 인덱스 번호가 일치할 때 stk
            strike_count += 1

        elif guesses[i] in solution:            # 위 조건 걸러지고 난 후 guesses[i] 가 solution에 포함될 때 ball
            ball_count += 1

    return strike_count, ball_count             # 값 2개로 리턴


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:
    tries += 1

    s_1, b_1 = get_score(ANSWER, take_guess())
    print(f"{s_1}S", f"{b_1}B")

    if s_1 == 3:
        print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞히셨습니다.".format(tries))
        break