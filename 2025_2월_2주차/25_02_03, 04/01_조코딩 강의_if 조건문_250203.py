# if 조건문
# "돈이 있으면 택시를 타고 가고, 돈이 없으면 걸어가라." <<< 이 문장이 if 반복문이 왜 사용되는지 알려주는 대표적인 문장이다.
# 위 문장을 if 반복문으로 풀어본다면...

money = True                  # 돈이 있는 상태를 의미
if money:                     # 돈이 있다면,
    print("택시를 타고 가라")  # 택시를 타고 가고
else:                         #그렇지 않으면,
    print("걸어가라")          # 걸어가라. 의 의미를 가지고 있음

'''
money = True
if money:
    print("택시를")
print("타고")             # 여기서 들여쓰기가 종료됨, if 반복문이 수행할 문장은 print("택시를") 밖에 없음.
    print("가라")         # 들여쓰기가 끊긴 상태에서 들여쓰기를 한다면 오류가 발생함.
'''
# 들여쓰기를 위 문장(폴더)에 대한 파일 이라고 생각하자.





# 조건문 이란?
# 조건문은 참과 거짓을 판별하는 문장 이라고 생각 하면 된다.
# 위 예제에서도 사용되었듯이
'''
money = True     # money 가 참 이기 때문에
if money:        # 만약 money 가 참이면 ~ 이란 if 문을 실행한다.
'''




# 비교 연산자
# 조건문에서 사용되는 비교 연산자(<, >, ==, !=, <=, >=) 를 알아보자.
'''
x < y - x 가 y 보다 작다.
x > y - x 가 y 보다 크다.
=========================
x == y - x와 y 는 같다.
x != y - x와 y 는 같지 않다.
x <= y - x 는 y 보다 작거나 같다.
x >= y - x 는 y 보다 크거나 같다.
'''
x = 3
y = 5
print(x < y) # True 가 출력 됨
print(x > y) # False 가 출력 됨


money = 2000                 # 2000 원
if money >= 3000:            # 만약 돈이 3000 원 보다 많거나 같다면
    print("택시를 타고 가라")  # 텍시를 타고 가고 (참 일경우.)
else:                        # 아니라면,(거짓일 경우.)
    print("걸어가라")         # 걸어가라.
# 거짓이기 때문에 걸어간다.


# 'and', 'or', 'not'
'''
x or y - x 나 y 둘 중 하나가 참이면 참
x and y - x 와 y 둘 다 참이어야 참.
not x - x 가 거짓이라면 참.
'''
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 가고, 그렇지 않으면 걸어가라." 해당 문장을 코드화 시키면,
money = 2000                   # 돈이 2000원 있고
card = True                    # card 가 있는 상태에서,
if money >= 3000 or card:      # 돈이 3000원 이상 있거나, or card 가 있다면, (or 문을 사용하여 card 참)
    print("택시 타고 가라")     # 택시를 타고 가라.
else:                          # 그게 아니면
    print("걸어가라")           # 걸어가라.

# 택시 타고 가라 


# and 활용

money = 2000                   # 돈이 2000원 있고
card = True                    # card 가 있는 상태에서,
if money >= 3000 and card:      # 돈이 3000원 이상 있고, and card 가 있다면, (and 문을 사용 : money = 거짓, card = 참 고로 해당 조건문은 '거짓')
    print("택시 타고 가라")     # 택시를 타고 가라.
else:                          # 그게 아니면
    print("걸어가라")           # 걸어가라
# 걸어가라                      # 거짓 수행문이 출력됨.


# not 활용

money = 2000                   # 돈이 2000원 있고
card = True                    # card 가 있는 상태에서,
if not card:                   # card 가 참이 아니라면 이라는 뜻 (card 는 참 이기에 해당 조건문의 결과는 False '거짓'이 됨)
    print("택시 타고 가라")     # 택시를 타고 가라.
else:                          # 그게 아니면
    print("걸어가라")           # 걸어가라
# 걸어가라                      # 거짓 수행문이 출력됨.




# in / not in
# 영 단어 ' ~ in ' 은 ' ~ 안에 ' 라는 뜻이다.
# in / not in 으로도 조건문을 만들 수 있다.
'''
x in [리스트] / x not in [리스트] - x 가 [리스트] 안에 있으면 '참' 없으면 '거짓' / x 가 [리스트] 안에 없으면 '참' 있으면 '거짓'
x in (튜플) / x not in (튜플) - x 가 (튜플) 안에 있으면 '참' 없으면 '거짓' / x 가 (튜플) 안에 없으면 '참' 있으면' 거짓'
x in "문자열" / x not in "문자열" - x 가 "문자열" 안에 있으면 '참' 없으면 '거짓'/ x 가 "문자열" 안에 없으면 '참' 있으면 '거짓'
'''
print(1 in [1, 2, 3]) # 1 이 리스트 [1, 2, 3] 안에 있나?
# True 결과 나옴
print(1 not in [1, 2, 3]) # 1 이 리스트 [1, 2, 3] 안에 없냐?
# False 결과 나옴
print('j' not in 'python') # 'j' 가 'python' 안에 없냐?
# True 결과 나옴

# in / not in 을 사용하여 택시 예제를 만들어보자.
# "주머니 안에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라."

poket = 'money', 'paper', 'cellphone'                 # poket 이라는 변수 안에 문자열 'money' 가 존재
if 'money' in poket:                                  # 만약 poket 이라는 변수 안에 'money' 가 있다면 (참)
    print('택시 타고 가라')                            # (참 이라면) 택시 타고 가고,
else:                                                 #(거짓 이라면) 아니면
    print("걸어가라")                                 # 걸어가라.
# 택시 타고 가라                                       # poket 변수 안 문자열 'money' 가 존재하므로 참 문장 수행.



# 리스트로도 만들어 보자

poket = ['cellphone', 'paper', 'money']              # 리스트 내 'money' 존재
if 'money' in poket:                                 # (참 이라면) poket 안에 money 가 있다면 
    print("택시 타고 가라")                           # 택시 타고 가고,
else:                                                # (거짓 이라면) 아니면
    print("걸어가라.")                                # 걸어가라.
# 택시 타고 가라                                      # poket 변수 내 리스트에 'money' 가 존재하므로 참 문장 수행.





# 조건문에서 아무 일도 하지 않게 설정하고 싶다면?
# 가끔 조건문의 참, 거짓에 따라 실행할 행동을 정의할 때나 아무런 일도 하지 않도록 설정하고 싶을 때가 있다.

# "주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라."
'''이럴 때 사용할 수 있는것은 'paas' 이다.'''

poket = ['money', 'card', 'cellphone']
if 'money' in poket:                # poket 안에 'money' 가 있기 때문에 (참 이기에)
    pass                            # 아무것도 실행되지 않고 넘어가며,
else:                               # poket 안에 'money' 가 없다면 (거짓 이라면)
    print('카드를 꺼내라.')          # '"카드를 꺼내라" 가 실행됨' 이지만 해당 결과값은 참 이기에, 아무런 결과값을 표시하지 않는다.



poket = ['money', 'card', 'cellphone']
if 'money' not in poket:            # poket 안에 'money' 가 없다면 ('money' 가 있기 때문에 해당 조건문은 '거짓')
    pass                            # 아무것도 실행되지 않고 넘어가며,
else:                               # poket 안에 'money' 가 있다면 (참) 이라면)
    print('카드를 꺼내라.')          # '"카드를 꺼내라" 가 실행됨' 참의 결과인 '카드를 꺼내라' 가 실행 됨

# pass 는 이렇게 아무것도 실행되지 않고 넘어가길 원할 때 사용된다.





# 다양한 조건을 판단하는 elif
# "주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라."
# 위 상황 처럼 조건이 여러 개 붙을 땐 'elif'를 사용함.

# 위 상황을 if/else만 사용한다면,

poket = ['cellphone', 'paper']
card = True
if 'money' in poket:             # 'poket' 안에 'money' 가 있으면
    print("택시 타고 가라")       # 택시 타고 가라 출력
else:                            # 그게 아니라면
    if card:                     # 만약 카드가 있으면 (참 이라면)
        print('택시 타고 가라')   # 택시 타고 가라 출력
    else:                        # 그게 아니라면 (거짓 이라면)
        print('걸어가라')         # 걸어가라 출력
# 택시 타고 가라
# 코드가 산만하고 복잡해 보인다.


# elif를 사용한다면,

poket = ['cellphone', 'paper']  # 주머니에는 폰과 종이가 있음.
card = True                     # 카드는 가지고 있음.
if 'money' in poket:            # 주머니 안에 돈이 있으면
    print('택시 타고 가라')      # 택시를 타고 가고
elif card:                      # 아니면 카드를 가지고 있어도
    print("택시 타고 가라")      # 택시를 타고 가라
else:                           # 그게 아니면,
    print('걸어가라')            # 걸어가라.
# 택시 타고 가라                 # 주머니 안에 돈은 없지만 카드 조건을 달성해서 택시를 타고 감.

# elif를 사용하면 깔끔해 보인다.





# elif는 개수 제한 없이 사용 가능하다.
# if / elif / else 를 사용한 기본 구조는 다음과 같다.
'''
if 조건문:
    수행할_문장1
    수행할_문장2

elif 조건문:
    수행할_문장1
    수행할_문장2
    
elif 조건문:
    수행할_문장1
    수행할_문장2

else:
    수행할_문장1
    수행할_문장2
'''


# if 문을 한 줄로 표현할 수 있다. # 굳이 사용 안함. # 패션 코딩 # 지적 허영심 채우는 용도

'''
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
'''


# 위 조건문을 한줄로 줄여보면
pocket = ['card', 'cellphone', 'paper']
if 'money' in pocket: pass
else: print("카드를 꺼내라라")
# 카드를 꺼내라




# 조건부 표현식 # 굳이 사용 안함. # 패션 코딩 # 지적 허영심 채우는 용도
 
score = 100

if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)
# success


# 위 코딩을 조건부 표현식으로 표현하자면

score = 100

message = "success" if score >= 60 else "failure"  # 일단 참일 때의 조건을 먼저 쓴다. > 그 다음에 조건을 쓴다. 

print(message)
# success


# 자료형의 참과 거짓
# 전 시간에 배웠던 ("", (), [], {}) 값이 비어있으면 거짓 들어있으면 참 (0 = 거짓 / None = 거짓)
# 조건문에 활용법

a = "python"             # if문 이라는게 True 면 실행되고 False 면 지나가야되는데 a 가 'python' 인데 이게 참 거짓을 판단할 수 있을까???

if a:
    print("참입니다.")

else:
    print("거짓입니다.")

# 참입니다.

# a의 값이 비어있지 않은 경우 참으로 판단 함.
