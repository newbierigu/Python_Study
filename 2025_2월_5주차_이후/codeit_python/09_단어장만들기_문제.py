# 영어 강사 Coy는 학생들의 단어 암기를 위해 단어장 프로그램을 만들려고 합니다. 
# 이 프로그램은 콘솔로 영어 단어와 한국어 뜻을 받고, vocabulary.txt라는 새로운 텍스트 파일에 단어와 뜻을 정리하는데요. 
# 사용자가 새로운 단어와 뜻을 입력할 때마다 vocabulary.txt에 작성되는 것입니다. 
# 사용자는 반복적으로 단어와 뜻을 입력하는데, 단어나 뜻으로 q를 입력하는 순간 프로그램은 즉시 종료됩니다. 
# 사용자가 q를 입력하고 나면 파일은 더 이상 바뀌지 않아야 합니다.

# 실행 결과 
# 1. 영어 단어를 입력하세요:
# 2. 영어 단어를 입력하세요: cat
# 3. 한국어 뜻을 입력하세요:
# 4. 영어 단어를 입력하세요: cat
# 5. 한국어 뜻을 입력하세요: 고양이
# 6. 영어 단어를 입력하세요:

# 이런 식으로 단어를 8개 입력했다고 가정합시다.

# 영어 단어를 입력하세요: cat
# 한국어 뜻을 입력하세요: 고양이
# 영어 단어를 입력하세요: apple
# 한국어 뜻을 입력하세요: 사과
# 영어 단어를 입력하세요: church
# 한국어 뜻을 입력하세요: 교회
# 영어 단어를 입력하세요: temple
# 한국어 뜻을 입력하세요: 절
# 영어 단어를 입력하세요: wallet
# 한국어 뜻을 입력하세요: 지갑
# 영어 단어를 입력하세요: backpack
# 한국어 뜻을 입력하세요: 책가방
# 영어 단어를 입력하세요: soap
# 한국어 뜻을 입력하세요: 비누
# 영어 단어를 입력하세요: bicycle
# 한국어 뜻을 입력하세요: 자전거
# 영어 단어를 입력하세요: q

# 사용자가 q를 입력하면 프로그램이 종료되고, vocabulary.txt에 다음과 같이 단어들이 정리되어 있어야 합니다.

# cat: 고양이
# apple: 사과
# church: 교회
# temple: 절
# wallet: 지갑
# backpack: 책가방
# soap: 비누
# bicycle: 자전거

with open("2025_2월_5주차_이후/codeit_python/data/vocabulary.txt", 'a', encoding='utf-8') as f: # 새로운 파일 생성 
    word = ''                                                                                  # 'a' 모드로 작성

    while word != 'q':                                  # word 가 'q'일때 종료
                                  
        word = input("영어 단어를 입력하세요: ")          # "영어 단어를 입력하세요: " word를 입력값을 받을 변수로 지정

        if word != 'q':                                 # word 가 'q'가 아닐 때
            f.write(f"{word}: ")                        # "word: "를 파일에 쓰고
            kor = (input("한국어 뜻을 입력하세요: "))     # 한국어를 입력받을 kor 변수 창조
            f.write(f"{kor}\n")                         # 한국어 받고 줄바꿈 처리를 위해 \n 작성.
