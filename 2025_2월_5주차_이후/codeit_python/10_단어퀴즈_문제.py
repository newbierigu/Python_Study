# 앞선 실습에서 vocabulary.txt라는 파일을 만들었죠? 이 파일에는 우리가 암기하고 싶은 단어들이 정리되어 있는데요. 
# 이번에는 이 파일의 단어들을 가지고 학생들에게 문제를 내는 프로그램을 만들려고 합니다.

# 프로그램은 터미널에 한국어 뜻을 알려 줄 것이고, 사용자는 그에 맞는 영어 단어를 입력해야 합니다. 
# 사용자가 입력한 영어 단어가 정답이면 맞았습니다!라고 출력하고, 틀리면 아쉽습니다. 
# 정답은 OOO입니다.가 출력되어야 합니다.

# 문제를 내는 순서는 vocabulary.txt에 정리된 순서입니다.

with open("2025_2월_5주차_이후/codeit_python/data/vocabulary.txt", 'r', encoding='utf-8') as f:
    word = []                           # 영단어 받을 리스트 변수 생성
    kor = []                            # 한국어 뜻 받을 리스트 변수 생성

    for line in f:                      # vocabulary.txt 값 분리하기.

        line = line.strip()             # 화이트 스페이스(\n) 제거
        word_split = line.split(": ")   # ": "로 단어 구분하기.

        word.append(word_split[0])      # 분리한 영단어 word리스트에 추가하기.
        kor.append(word_split[1])       # 분리한 한국어 뜻 kor리스트에 추가하기.

for i in range(len(kor)):               # kor 리스트 길이로 문제 수 조절

    answer = input(f"{kor[i]}: ")       # kor 요소 하나씩 순서대로 출력 후 입력값 받기.

    if answer == word[i]:               # answer == 지정된 영단어와 같다면, 
        print("맞았습니다!")

    else:                               # 다르다면, 
        print(f"아쉽습니다. 정답은 {word[i]}입니다.")



# 정답 2
"""
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))
"""