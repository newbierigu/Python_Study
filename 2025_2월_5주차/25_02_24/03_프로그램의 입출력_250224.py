# 프로그램의 입출력
# doit 폴더 안에 sys1.py 파일에 밑에 있는 명령어들이 있음.
# debug 창에서 실행함


# sys1.py 뒤에 1 2 3 숫자를 붙였을 때 그 뒤에 붙인 숫자들을 출력 함
# python .\sys1.py 1 2 3
# 1
# 2
# 3

'''
import sys

args = sys.argv[1:]
for i in args:
    print(i)
'''


# sys1.py 뒤에 붙인 숫자들을 전부 더함
# python .\sys1.py 2 4 6
# 12

'''
import sys

sum = 0
args = sys.argv[1:]
for i in args:
    sum = sum + int(i)
print(sum)
'''


# sys1.py 뒤에 문자를 대문자로 변경한다.
# python .\sys1.py life is too short
# LIFE IS TOO SHORT

'''
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end =' ')
'''