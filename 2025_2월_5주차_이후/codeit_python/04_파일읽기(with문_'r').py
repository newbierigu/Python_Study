with open('2025_2월_5주차_이후/codeit_python/data/chicken.txt', 'r', encoding='utf-8') as f:    # 파일을 읽어오기 위한 명령어 읽어드린 파일을 변수 f에 저장함
                                            # with open 파일을 열어서 'r'read의 약자 읽는다.
    print(type(f))
# <class '_io.TextIOWrapper'> 로 나온다.
# 문자열도 아니고 리스트도 아닌데 어떻게 불러올 수 있을까?

# 리스트는 아니지만 for 문을 사용하면 리스트와 비슷하게 불러올 수 있다. # encoding=utf-8로 해야한다.
    for line in f:
        print(line)