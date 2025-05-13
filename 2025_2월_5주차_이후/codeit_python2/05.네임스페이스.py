# 네임 스페이스는 파일에서 정의된 모든 이름들을 뜻함.
# 결국 dir 함수는 파일의 네임 스페이스를 리턴해주는 것.
"""
from area import circle, square 

print(dir())
"""
# 현재 파일의 네임 스페이스는
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'circle', 'square'] 로 이루어져 있다.

# 그런데 지금 이 파일에서 또 다른 square함수를 정의하면 어떻게 될까?

# 정사각형 둘레를 구해주는 함수 정의하기.
'''
def square(length):
    return length * 4

print(square(3))
'''
# 결과는 넓이 9가 아닌 둘레 값 12 가 나온다.
# 정사각형의 넓이를 구해주는 area 모듈의 square 함수가 아닌 둘레를 구해주는 함수 square 가 사용되었다.
# 파이썬에서는 동일한 이름을 가진 함수를 사용했을 때 제일 나중에 정의된 함수를 사용한다.

# 한 네임 스페이스 안에서는 같은 이름이 중복되지 않는것이 좋다.

# 중복 안되는 방법
# 1. 모듈에서 square 함수를 가져올 때 이름을 바꿔주는 것.
'''
from area import circle, square as sq

def square(length):
    return length * 4

print(dir())
print(square(3))
print(sq(3))
'''
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'circle', 'sq', 'square'] 네임 스페이스가 따로 나눠져서 나오는 것을 확인할 수 있고, 
# 12 정사각형 둘레 값
# 9  정사각형 넓이 값 따로 출력되는 것을 확인할 수 있다.


# 2. 모듈 그대로 임포트 하는 방법.
"""
import area

def square(length):
    return length * 4

print(dir())
print(square(3))
print(area.square(3))
"""
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
#  'area', 'square'] area 와 square가 따로 나눠져서 나오는 것을 확인할 수 있고,
# 12 정사각형 둘레 값
# 9  정사각형 넓이 값 따로 출력되는 것을 확인할 수 있다.


# 참고로 from area import * 로 했을 땐,

from area import *

def square(length):
    return length * 4

print(dir())
print(square(3))

# ['PI', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'circle', 'square']  PI, circle, square 가 전부 나온다. area모듈에서 정의된 모든 이름들을 네임 스페이스에 추가한다.
# 넓이 값이 아닌 12 둘레 값이 추가된다. 
# 이 처럼 네임 스페이스에 어떤 이름들이 추가됐는지 파악하기 힘들어지고 같은 이름들이 중복될 확률이 높아진다.
# 그래서 import *은 권장하지 않는 방법이다.