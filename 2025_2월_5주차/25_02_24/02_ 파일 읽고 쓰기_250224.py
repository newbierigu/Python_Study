# 파일 읽고 쓰기

# open 함수(파일 객체를 만들어 줄 때 사용하는 함수)

'''
f = open("새 파일.txt", "w")                                                                                                                                                                
f.close()
'''
# 위 함수처럼 파일 위치를 설정해주지 않으면 명령어를 사용한 스크립트가 있는 위치에 파일을 생성함

# 파일 위치 지정하기(doit폴더)
'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'w')
f.close()
'''
# doit이라는 폴더 안에 '새 파일.txt' 파일이 생성 됨

'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)

f.close()
'''

# 새 파일 열면 1번째 줄입니다. ~ 10번째 줄입니다. 출력됨

# 추가 지식 : 위 예시로 파일 생성 후 VSC로 열었을 때 ?@#$!@%$ 이런식으로 깨져있는 경우, encoding이 안되서 그렇다.
'''
f = open("새 파일.txt", 'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)

f.close()
'''
# 현 폴더에 있는 새 파일 확인해보자. 글자가 그대로 나올것이다. 한글은 UTF-8로 인코딩 해줘야 함.








# 파일을 읽는 여러가지 방법

# 함수 readline 사용하기
'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'r')
line = f.readline()
print(line)
f.close()
'''
# 1번째 줄입니다.
# readline 함수는 한 줄만 가져옴.





# 여러 줄을 가져올 때  반복문 사용으로 가져 옴옴
'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''
# 1번째 줄입니다.
# 2번째 줄입니다. ...
# 10번째 줄입니다.



# readlines 함수 이용하기
# readlines는 변수 안에 파일 안에 있는 요소 값을 '리스트'에 담아서 리턴해준다.
'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'r')
lines = f.readlines()    # f 에 해당되는 파일에 요소를 리스트화 시킨다.
for line in lines:       # line이라는 변수 안에 리스트 요소를 하나씩 담는다.
    print(line)          # 변수 line 출력
f.close()
'''
# 1번째 줄입니다.
# 2번째 줄입니다. ...
# 10번째 줄입니다.



# read 함수 이용하기
# read 함수는 통째로 다 가져오는 함수다.
'''
f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'r')
data = f.read()
print(data)
f.close()
'''
# 1번째 줄입니다.
# 2번째 줄입니다. ...
# 10번째 줄입니다.



# 파일에 새로운 내용 추가하기 'a' 모드
# 'w' 모드는 기존에 있던 파일에 덮어씌우는 반면,
# 'a' 모드는 기존에 있던 값을 유지하면서 새로운 값을 추가한다.

'''
f = f = open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다. \n" % i
    f.write(data)           # f 에 해당하는 파일에 data 값을 쓰겠다.
f.close()
'''

# 실행하면 기존에 1 ~ 10번째 줄 에서 >>> 1 ~ 19번째 줄입니다 까지 추가 됨.


 
# with 문 활용하기
# open/close 를 자동으로 해준다.

with open("C:/Users/nuwba/Desktop/파이썬 공부/2025_2월_5주차/25_02_24/doit/새 파일.txt", 'a') as f:
    data = "Life is too short, you need python."
    f.write(data)

# 'a'모드로 "Life is too short, you need python." 문구 추가하여 1 ~ 19번째 줄입니다. 다음에 "Life is too short, you need python." 문장 추가됨.







