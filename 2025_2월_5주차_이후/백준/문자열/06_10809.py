# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.


'''풀이 과정
문제 이해
1. 임의의 단어 입력 받을 변수 창조
2. a ~ z 까지의 알파벳이 입력한 단어의 처음으로 등장하는 인덱스 위치가 어딘지 출력하는 코드 생성이 목적 (없으면 -1 출력)
ex) 입력 : baekjoon
    출력 : (a)1 (b)0 (c)-1 (d)-1 (e)2 -1 -1 -1....
'''

word = input()                                  # 임의의 단어 입력 자리 변수 생성

for i in range(97, 123):                        # 아스키 코드를 사용하여 하나씩 i에 대입하여 word 와 알파벳 대조
    if chr(i) not in word:                      # 만약 word 안에 포함되있지 않다면
        print(-1, end = ' ')                    # -1을 출력하고 공백으로 구분
    else:
        print(word.index(chr(i)), end = ' ')    # 포함되있으면 처음으로 등장한 그 알파벳의 index 자리 값 출력 
