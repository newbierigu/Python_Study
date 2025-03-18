# 피보나치 수열 공부

'''
def Fibonacci_Sequence(n):
    i = 1
    j = 0
    for _ in range(n):
        i, j = j, i + j
        if i == 0:
            continue
        else:
            print(i)


Fibonacci_Sequence(51)
'''

previous = 0
current = 1
i = 1

while i <= 50:
    print(current)
    temp = previous  # previous를 임시 보관소 temp에 저장
    previous = current
    current = current + temp  # temp에는 기존 previous 값이 저장돼 있음
    i += 1


