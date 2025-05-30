# 문제
# 아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 
# 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다. 
# 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다. 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다. 
# 이런 식으로 다섯 개의 단어를 만든다. 
# 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다. 

# A A B C D D
# a f z z 
# 0 9 1 2 1
# a 8 E W g 6
# P 5 h 3 k x

# <그림 1>

# 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 
# 심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다. 
# 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다. 다음에 두 번째 글자들을 세로로 읽는다. 
# 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다. 
# 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다. 
# 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다. 
# 그림 1에서 영석이가 세로로 읽은 순서대로 글자들을 공백 없이 출력하면 다음과 같다:
# Aa0aPAf985Bz1EhCz2W3D1gkD6x
# 칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.



# 입력
# 총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 
# 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.


# 출력
# 영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다. 


'''풀이 과정
공백은 무시하고 붙여버림
입력은 공백없이 5회가 주어짐 각 줄의 시작과 마지막 줄엔 공백은 없다

5회 입력할 공간 만들기
word = []                                           # word 리스트 변수 생성
answer_word = ''

for _ in range(5):
    word.append(list(map(str,input().split())))     # 입력 값을 리스트 형태로 받아서 word에 추가

여기서 내 생각

일단 5번의 입력을 받고 입력되는 문자의 수는 랜덤
ex) aadt
    aaddf
    sd
    2dv
    avvnf
입력이 이런식으로 됐으면

word 리스트에 [['a','a','b','t'], ['a','a','d','d','f'], ['s','s'], ['2','d','v'], ['a','v','v','n','f']]
이렇게 담김

그럼 for 반복문으로 변수 생성해서 하나씩 뽑자 라는 생각인데 여기서 문제가 발생함
만약 for n in range(16):                         # 16인 이유는 한 줄에 입력할 수 있는 범위가 1 ~ 16 이어서
이러면 out of range 오류가 난단말이지..

# 위 상황의 해결 방법 생각들
1. for i in range(5): 를 사용해서
word 내 요소들의 길이 = n 으로 해서  word[i][n] 이런식으로 한글자 씩 번갈아서 뽑은 후 answer_word에 하나씩 추가
2. 여기서도 n을 어떻게 만들어줘야할까 고민..
3. n = len(word[i]) 이렇게 만들면 될까?

for i in range(5):
    n = len(word[i]) - 1
    for _ in range(n)
    word[i][n] += answer_word
    이러면 이상하지

word 내 요소들 중 최대 길이를 구하고
만약 반복 기록 하다가 그 길이를 넘어가면 무시하고
아니면 계속 반복기록 하게끔 만들면 될거같은데

    
어떻게 하면 될까?

'''
word = []                                           # 입력 값을 리스트화 해서 저장할 word 리스트 변수 생성
answer_word = ''                                    # word 요소(리스트) 내 요소에서 값을 하나씩 뽑아 정답을 리턴할 answer_word 변수 생성

for _ in range(5):                                  # 5번 입력 할 변수 생성
    word.append(list(input()))                      # 입력한 요소들을 리스트화 해서 word 리스트에 추가


                           
max_length = max(len(row) for row in word)          # 가장 긴 word 요소의 길이 구하기

for j in range(max_length):                         # 열(세로) 기준으로 반복
    for i in range(5):                              # 행(가로) 기준으로 반복
        if j < len(word[i]):                        # 현재 단어의 길이를 초과하면 무시
            answer_word += word[i][j]    

print(answer_word)