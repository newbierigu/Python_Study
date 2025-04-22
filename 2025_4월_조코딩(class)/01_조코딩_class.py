# calculator.py
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num   # 결과값(result)에 입력값(num) 더하기
    return result1   # 결과값 리턴

def add2(num):
    global result2
    result2 += num 
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))


# 위 코드와 같이 만약 계산기가 2개가 각각 필요할 때 똑같은 함수와 똑같은 변수를 2개씩 만들어서 사용한다.
# 만약 계산기가 100개 아님 1000개 일 때 이걸 다 만들어야되나? 이건 비효율적이다.
# 그래서 나온 개념이 class이다.
# 진도 02에서 위 계산기에 class 개념을 접목시켜보자.