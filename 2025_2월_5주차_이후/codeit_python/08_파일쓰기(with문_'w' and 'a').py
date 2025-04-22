'''
with open('2025_2월_5주차_이후/codeit_python/data/new_file.txt', 'w') as f:

    f.write("Hello world")
    f.write("My name is Rigu")  
# 위 경로에 new_file.txt 파일이 생기며, 'Hello worldMy name is Rigu' 로 입력되어있다.

# 만약 Hello worldMy name is Rigu를 구분하고 싶으면 어떻게 할까?
    f.write("Hello world\n")
    f.write("My name is Rigu")
# Hello world
# My name is Rigu로 정상 출력된다.
'''

    # 그런데 분명 프로그램을 2번 실행했는데 누적이 안되고 기존 내용이 지워지고 저렇게 출력됐다.
    # 만약 내용을 누적시키고 싶다면 어떻게 할까?

# with문에서 'w' 대신 'a' append를 넣어주면 된다.
with open('2025_2월_5주차_이후/codeit_python/data/new_file.txt', 'a') as f:
    f.write("\nMy hobby is LOL/MHW\n")
    f.write("and coding")
# Hello world
# My name is Rigu
# My hobby is LOL/MHW
# and coding으로 누적되어 정상 출력된다.

# 파일이 없을때도 'w' 대신에 'a'를 써도 상관 없이 파일 쓰기가 가능하다.