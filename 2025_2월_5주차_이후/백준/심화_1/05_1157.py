# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 
# 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

'''풀이 과정
문제 이해
1. 대/소문자 구분없이 단어 내 가장 많이 쓰인 알파벳 대문자로 출력
2. 만약 단어 내 많이 사용한 문자 2개 이상 일 시 ? 출력
'''

word = input().upper()                      # 대/소문자 구분 없애기
a_count = {}                                # 알파벳 개수를 저장할 딕셔너리

for alpabet in word:
    if alpabet in a_count:  
        a_count[alpabet] += 1               # 이미 있으면 개수 증가
    else:
        a_count[alpabet] = 1                # 처음 등장하는 문자면 1로 초기화

max_count = max(a_count.values())           # 최댓값 찾기
most_used = [key for key, value in a_count.items() if value == max_count]

if len(most_used) > 1:
    print("?")                  # 최댓값을 가진 문자가 여러 개면 ?
else:
    print(most_used[0])         # 가장 많이 사용된 알파벳 출력





