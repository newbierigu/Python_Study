# 사용자 입력 받기 : input
# 유저에게 입력을 받기위해서 사용함

a = input()
print(a)

# 주의 사항
'''
x = input()
print(x + 5)
'''
# 위 코드는 오류가 발생한다. input으로 들어간 값은 무조건 str형이다.
# 그러므로 str + int가 되어 오류가 발생한다
# 해결 방법은 str을 int로 바꿔주는 int(input())을 사용하면 된다.