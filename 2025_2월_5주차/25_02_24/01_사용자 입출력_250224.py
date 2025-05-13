# 사용자 입출력
# 사용자의 입력에 따라 그에 맞는 출력을 내보낸다.


# input 함수

'''
a = input()

print(a)
'''

# 입력 : hello Wolrd
# 출력 : hello Wolrd

'''
number = input("숫자를 입력하세요 : ")

print(number)

print(type(number))
'''

# 입력 : 숫자를 입력하세요 : 3
# 출력 : 3
# <class 'str'>    input에 입력되는 모든 값은 문자열로 취급한다.



# print 자세히 알기

print("Life" "is" "too short")  # 1번
print("Life" + "is" + "too short")   # 2번


# 1/2번 결과 Lifeistoo short로 동일함 

# 문자열 띄어쓰기를 할 때는 , 로

print("Life", "is", "too short")

# Life is too short 결과 출력 됨



# 한 줄에 결과 표시하기

for i in range(10):
    print(i, end = ' ')

# 0 1 2 3 4 5 6 7 8 9

# print는 기본적으로 한 칸 띄어서 한 줄을 차지함
# end = ' ' <<< 출력 후 끝에 ' ' 를 출력하겠다 란 뜻 그래서 한 줄로 출력 됨.
