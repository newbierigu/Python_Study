'''
1과 20 사이의 숫자를 맞히는 게임을 만들려고 합니다. 
random 모듈과 input() 함수를 활용하여 프로그램을 만들어 보세요.

진행 방식
1. 프로그램을 실행하면 기회가 *번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요:가 출력됩니다. 
   총 네 번의 기회가 주어지며, 사용자가 한 번 추측할 때마다 남은 기회가 줄어듭니다.
2. 정답을 맞히면 축하합니다. *번 만에 숫자를 맞히셨습니다.가 출력되고 프로그램은 종료됩니다.
   사용자가 입력한 수가 정답보다 작은 경우 Up이 출력되고, 입력한 수가 정답보다 큰 경우 Down이 출력됩니다.
3. 정답이 틀렸으면 1번부터 다시 진행합니다. 
   만약 네 번의 기회를 모두 사용했는데도 답을 맞히지 못했으면, 아쉽습니다. 정답은 *입니다.가 출력되고 프로그램은 종료됩니다.
'''
# 정답 1
import random

x = random.randint(1, 20)                                                     # 1~20 정수 랜덤 선정
answer_count = 1                                                              # 답변 횟수 카운트할 변수 생성
chance = 3                                                                    # 정답 기회 변수 생성

for _ in range(chance + 1):                                                   # for 반복문 사용
    y = int(input(f"{chance + 1}번 남았습니다. 1-20 사이의 숫자를 맞혀보세요:")) # 문제 및 입력 받을 변수 생성

    if x == y:                                                                # 정답 시 조건
        print(f"축하합니다. {answer_count}번 만에 숫자를 맞히셨습니다.")         # 정답 문구 출력 및 답변 횟수 출력
        break
    if chance == 0:                                                           # 정답 기회 모두 소진 시 조건
        print(f"아쉽습니다. 정답은 {x}입니다.")                                 # 오답 문구 출력 및 정답 공개

    if x > y:                                                                 # 입력 값이 답 보다 작을 때 조건
        print("Up")                                                           # 'Up' 문구 출력
        answer_count += 1                                                     # 답변 횟수 증가
        chance -= 1                                                           # 답변 기회 감소
        continue                                                              # 반복문 처음부터 다시 시작
    elif x < y:                                                               # 입력 값이 답보다 작을 때 조건
        print("Down")                                                         # 'Down' 문구 출력 및 이하 동문
        answer_count += 1
        chance -= 1
        continue

# 정답 2
'''
import random

# 상수 정의
ANSWER = random.randint(1, 20)
NUM_TRIES = 4

# 변수 정의
guess = -1
tries = 0

while guess != ANSWER and tries < NUM_TRIES:
    guess = int(input("기회가 {}번 남았습니다. 1-20 사이의 숫자를 맞혀 보세요: ".format(NUM_TRIES - tries)))
    tries += 1    
    
    if ANSWER > guess:
        print("Up")
    elif ANSWER < guess:
        print("Down")

if guess == ANSWER:
    print("축하합니다. {}번 만에 숫자를 맞히셨습니다.".format(tries))
else:
    print("아쉽습니다. 정답은 {}입니다.".format(ANSWER))
'''