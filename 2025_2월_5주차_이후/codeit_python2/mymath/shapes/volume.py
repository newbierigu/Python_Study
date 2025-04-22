'''
# 공부 진도 15에 해당되는 코드(__init__)
from mymath.shapes import PI
'''

# 공부 진도 16에 해당되는 코드
__all__ = ['sphere', 'PI']

PI = 3.14

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius * radius


# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length