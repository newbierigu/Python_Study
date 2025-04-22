# 지난 실습 과제에서 단어장 퀴즈 프로그램을 만들었는데요. 
# 학생들이 문제의 순서가 매번 똑같아서 재미가 없다고 합니다. 
# 이번에는 random 모듈과 사전(dictionary)을 이용해서 
# vocabulary.txt의 단어들을 랜덤한 순서로 문제를 내도록 프로그램을 바꿔 보세요. 
# 같은 단어를 여러 번 물어봐도 괜찮고, 프로그램은 사용자가 알파벳 q를 입력할 때까지 계속 실행됩니다.

import random

with open("2025_2월_5주차_이후/codeit_python/data/vocabulary.txt", 'r', encoding='utf-8') as f:
    
    answer_sheet = {}

    for line in f:
        data = line.strip().split(": ")
        answer_sheet[data[1]] = data[0]

answer = ''

while answer != 'q':
        random_que = random.choice(list(answer_sheet.keys()))
        answer = input(f"{random_que}: ")

        if answer != 'q':
            if answer == answer_sheet[random_que]:
                print("맞았습니다!")

            else: 
                print(f"틀렸습니다. 정답은 {answer_sheet[random_que]}입니다.")

        else:
             break
        

# 정답 2
"""
import random

# 사전 만들기
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# 목록 가져오기
keys = list(vocab.keys())

# 문제 내기
while True:
    # 랜덤한 문제 받아 오기
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # 유저 입력값 받기
    guess = input("{}: ".format(korean_word))
    
    # 프로그램 끝내기
    if guess == 'q':
        break
    
    # 정답 확인하기
    if guess == english_word:
        print("정답입니다!\n")
    else:
        print("틀렸습니다. 정답은 {}입니다.\n".format(english_word))
"""