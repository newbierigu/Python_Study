'''
a, b = map(int,input().split())

if a > b:
    print('>')

elif a < b:
    print('<')

elif a == b:
    print('==')
'''


'''
score = int(input())

if score >= 90:
    print('A')

elif score <= 89 and score >= 80:
    print('B')

elif score <= 79 and score >= 70:
    print('C')

elif score <= 69 and score >= 60:
    print('D')

else:
    print('F')
'''





# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때다.
'''
year = int(input())


if year % 4 == 0 and year % 100 != 0:
    print(1)

elif year % 400 == 0:
    print(1)

else:
    print(0)

'''

'''
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)

elif x < 0 and y > 0:
    print(2)

elif x < 0 and y < 0:
    print (3)

else:
    print(4)

'''

# 24시간 형태로 시간이 주어지고
# 시간 입력 후 + 45 된 시간으로 결과값이 나오도록 유도하는 프로그램
# 0 ~ 24 시 범위
# 0 ~ 59 분 범위

"""
입력된 시간 - 45분




m - 45 < 0            만약 45분을 뺐을 때 음수가 된다면 
    h -= 1            # 1시간 빼주고
    print(h, abs(m))  # 절대 값으로 변경하여 출력




if m == 0:             # 만약 m 이 0일 경우 - 45분을 해야한다면
    m = 60
    m - 45
    h - 1
    print(h, m)


m - 45가 음수가 됐을 때

60 - (45 - 10)




"""
'''
h, m = map(int,input().split()) 

if m >= 0:
    m -= 45
    
    if m > 0:
        print (h, m)

    elif m < 0:
        m += 45
        m = 60 - (45 - m)
        h -= 1
        if 24 > h >= 0:
            print(h, m)
        elif h < 0:
            h = 23
            print(h, m)

    elif m == 0:
        print(h, m) 
'''





"""
t 를 시간 분으로 쪼개줌
th = t // 60
tm = t % 60

현재 시에 th 더해줌
h += th

이게 24 초과면
if h > 23:
    h = h - 24

현재 분 에 tm 더해 줌
m += tm

이게 60 초과면
if m > 59:
    h + 1
    m = m - 60

"""




'''
h, m = map(int,input().split())
t = int(input())

th = t // 60
tm = t % 60

m += tm
if m > 59:
    h += 1
    m = m - 60

h += th
if h > 23:
    h = h - 24
    
print(h, m)
'''





'''
a, b, c = map(int,input().split())

# 같은 눈 3개 공식
if a == b == c:
    print(10000 + a * 1000)

# 같은 눈 2개 공식
elif a == b or a == c:
    print(1000 + a * 100)

elif b == c:
    print(1000 + b * 100)

# 모두 다른 눈 공식
else:
    print(max(a, b, c) * 100)
'''