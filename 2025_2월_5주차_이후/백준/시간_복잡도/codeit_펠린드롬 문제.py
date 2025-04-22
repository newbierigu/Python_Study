# 펠린드롬 확인
def is_palindrome(word):
    if word == word[::-1]:         # 만약 word 랑 word의 반대로 나열한것과 같다면
        result = True              # result = True
    else:                          # 다르다면,
        result = False             # result = False
    
    return result

# 테스트 코드
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))






'''
def mask_security_number(security_number):

    security_number = security_number[:-4] + '****'

    return security_number

# 테스트 코드
print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))
'''



'''
# 자리수 합 리턴
def sum_digit(num):
    num = str(num)
    sum_num = 0
    for i in range(len(num)):
        sum_num += int(num[i])
    return sum_num


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
answer = 0
for i in range(1, 1001):
    answer += sum_digit(i)
    
print(answer)'''

'''
# 투표 결과 리스트
votes = ['김영자', '강승기', '최만수', '김영자', '강승기', '강승기', '최만수', '김영자', \
'최만수', '김영자', '최만수', '김영자', '김영자', '최만수', '최만수', '최만수', '강승기', \
'강승기', '김영자', '김영자', '최만수', '김영자', '김영자', '강승기', '김영자']

# 후보별 득표수 사전
vote_counter = {}

# 리스트 votes를 이용해서 사전 vote_counter를 정리하기
for name in votes:
    vote_counter[name] = 0

for key in votes:
    vote_counter[key] += 1
 

# 후보별 득표수 출력
print(vote_counter)
'''



'''
# 언어 사전의 단어와 뜻을 서로 바꿔주는 함수
def reverse_dict(old_dict):
    new_dict = {}  # 새로운 사전
    
    # old_dict의 key와 value를 뒤집어서 new_dict에 저장
    for key, value in old_dict.items():
        new_dict[value] = key
    
    return new_dict  # 변환한 새로운 사전 리턴

# 영-한 단어장
vocab = {
    'sanitizer': '살균제',
    'ambition': '야망',
    'conscience': '양심',
    'civilization': '문명',
    'privilege': '특권',
    'principles': '원칙'
}

# 기존 단어장 출력
print("영-한 단어장\n{}\n".format(vocab))

# 변환된 단어장 출력
reversed_vocab = reverse_dict(vocab)
print("한-영 단어장\n{}".format(reversed_vocab))
'''






'''
# 1. 단어장 만들기
vocab = {
    'sanitizer' : '살균제', 'ambition' : '야망', 
    'conscience' : '양심', 'civilization' : '문명'
}
print(vocab)


# 2. 새로운 단어들 추가
vocab['privilege'] = '특권'
vocab['principle'] = '원칙'

print(vocab)
'''