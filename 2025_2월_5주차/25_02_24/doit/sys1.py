
# 1번 파일 명 뒤 숫자 나열하기
'''
import sys

args = sys.argv[1:]
for i in args:
    print(i)
'''

# 2번 파일 명 뒤 숫자 더하기
'''
import sys

sum = 0
args = sys.argv[1:]
for i in args:
    sum = sum + int(i)
print(sum)
'''


# 3번 파일 명 뒤 문자열 대문자로 변경
'''
import sys

args = sys.argv[1:]
for i in args:
    print(i.upper(), end =' ')
'''



import sys

sum = 0
args = sys.argv[1:]
for i in args:
    sum += int(i)
print(sum)