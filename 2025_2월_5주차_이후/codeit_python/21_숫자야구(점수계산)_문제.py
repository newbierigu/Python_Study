# 이제 스트라이크 수와 볼 수를 알려 주는 get_score() 함수를 작성할 것입니다. 
# 이 함수는 두 개의 파라미터를 받는데요.

# guesses: 유저가 뽑은 번호 3개가 담긴 리스트
# solution: 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
# 두 리스트를 비교해서 스트라이크와 볼의 개수를 계산하고 리턴합니다. 
# 여기서 새로운 개념을 알려 드릴게요. 파이썬의 함수에서 여러 값을 리턴하고 싶으면 이렇게 할 수 있습니다.

# def square_and_cube(x):
#     square = x ** 2
#     cube = x ** 3
#     return square, cube

# 또한 여러 리턴 값을 한 번에 여러 변수에 저장할 수도 있습니다. 
# square_and_cube(2)의 첫 번째 리턴 값이 변수 s에 저장되고, 두 번째 리턴 값이 변수 c에 저장됩니다.

# s, c = square_and_cube(2)
# print(s)
# print(c)

# 이런 식으로 get_score() 함수는 스트라이크와 볼의 개수를 모두 리턴하도록 해야 합니다. 
# 예를 들어서 아래 코드를 실행해 볼게요.

# s, b = get_score([2, 7, 4], [2, 4, 7])
# print(s)  # 스트라이크 수 출력
# print(b)  # 볼 수 출력

# 2는 숫자의 값과 위치가 모두 일치하기 때문에 스트라이크입니다. 
# 그리고 7과 4의 경우, 숫자의 값은 일치하지만 위치가 틀렸기 때문에 볼입니다. 
# 스트라이크 1개와 볼 2개니까, 정수 1과 2를 모두 리턴해야 하는 거죠. 



def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    for i in range(len(solution)):
        
        if guesses[i] == solution[i]:           # guesses 와 solution의 요소 값과 인덱스 번호가 일치할 때 stk
            strike_count += 1

        elif guesses[i] in solution:            # 위 조건 걸러지고 난 후 guesses[i] 가 solution에 포함될 때 ball
            ball_count += 1

    return strike_count, ball_count             # 값 2개로 리턴

s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])     
print(s_1, b_1)             # 리턴한 값을 s_1, b_1 순서대로 넣어줌. 새로운 개념이니 잘 이해하고 써먹자.

s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
print(s_2, b_2)

s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
print(s_3, b_3)

s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
print(s_4, b_4)