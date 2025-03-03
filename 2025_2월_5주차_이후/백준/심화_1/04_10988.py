# 문제
# 알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
# level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

# 입력
# 첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.


'''풀이 과정
일단 처음 input 받을 공간 마련 후 (word = input())
# 나중에 든 생각 : 받을 때 부터 리스트 화 시키자 ( word = list(map(str,input())) )
그 다음이 문제...

단어가 홀수이면
가운데 글자 포함 앞 문자가 뒷 문자 역순과 같아야되고

단어가 짝수면
절반씩 앞 문자가 뒷 문자가 역순과 같아야되는데

구현을 어떻게 하지..?

1. 일단 word에 들어간 단어 수를 파악해보자
   그럴 필요가 있나 싶지만 일단은 해보자
   그럴려면 단어 개수를 담을 변수도 만들자 (= word_count = 0)
   for _ in word:
       word_count += 1
 
2. 그러고 홀수/짝수 함수를 만들어서 따로 실행시켜보자
   def odd_even()

3. 그리고 그 안에서 
   팰린드롬(Palindrome) 인지 아닌지 파악하는 공식을 만들어야된다.
   음.... 이게 제일 큰 문제네
   천천히 해보고
   마지막에 '1'을 출력할지, '0'을 출력할지 정하자

만들다가 완전 뻘짓거리한걸 깨달았다

그냥 문자 홀수든 짝수든 뒤집었을 때 

안뒤집은거랑 똑같으면 1
            다르면   0
출력하면 된다...

만들자..

'''


# 정답 1
'''
word = list(map(str,input()))

def Palindrome():
    result = ''
    word_mirror = []
    
    for i in reversed(word):
        word_mirror += [i]
    
    if word == word_mirror:
        result = '1'
    else:
        result = '0'
    
    return result

print(Palindrome())
'''



# 정답 2
word = input()
print(1 if word == word[::-1] else 0)








'''
중간에 깨달아서 망정이지 그거 아니었으면 짝수 패턴도 만들 뻔
멍청하면 몸이 힘들다.
생각 쉽게쉽게 하자 다음부터..
뻘짓거리 증거

def odd_word():
    result = ''
    word_head = []
    word_tail = []

    word_mid_ind = 0
    word_middle = word[(word_count - 1) // 2]
    for i in word:
        word_mid_ind += 1
        if i == word_middle:
            word_mid_ind -= 1
            break

    for j in range(0, word_mid_ind + 1):       
        word_head += [word[j]]

    for k in range(word_mid_ind, word_mid_ind * 2 + 1): 
        word_tail += [word[k]]
    
    word_tail.reverse()

    if word_head == word_tail:
        result = '1'
    else:
        result = '0'

    return result
'''