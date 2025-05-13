# chicken 내 문자들은 453400\n 이렇게 이뤄져있기 때문에 그대로 불러오면 한 줄씩 띄어서 출력된다.
# ex
print("Hello\n")
print("Hello")

# 빈 줄들을 어떻게 처리할까?
# 문자열에서 배운 strip을 사용해보자.
# strip은 어떤 문자열에서 앞뒤로 있는 화이트 스페이스를 없에주는 역할을 한다.
# 화이트 스페이스 = " ", "\t", "\n"

print("       abc   def       ".strip())
# 좌우 공백을 자 삭제함

print("     \t   \n   abc   def\n\n\n".strip())
# 마찬가지로 좌우 공백 삭제

# 파일 불러오기에 적용해보자
with open('2025_2월_5주차_이후/codeit_python/data/chicken.txt', 'r', encoding='utf-8') as f: 
    for line in f:
        print(line.strip())