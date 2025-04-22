# 유용한 내장함수 dir
# dir : 어떤 파일 안에서 정의된 모든 이름들을 알려주는 함수
'''
import area

print(dir(area))
'''
# ['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'circle', 'square']
# PI, circle, square
# area 파일 내 정의된 이름들을 전부 알려준다.
# 여기에 이름 양 옆에 언더스코어(_)가 2 개씩 붙어있는 애들이 있다.

# 이것들을 특수 변수 라고 부는다.(던더 라고 부른다. (더블언더스코어 줄임말) 던더 파일)
# 특수 변수는 파이썬이 내부적으로 관리하는 변수이다.


# 이번엔 dir 함수를 사용하여 현재 이 파일에서 정의된 이름들을 확인해보자
'''
import area
print(dir())
'''
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
#  'area']
# 이번에도 다양한 특수 변수들이 나오고, 맨 뒤에 area가 나온다.
# 모듈을 임포트하면 이 파일에서는 모듈의 이름만 정의되고, 모듈 안에 있는 함수나 변수에 이름들은 정의되지 않는다.
# PI, circle, squaer은 여기서 나타나지 않는다.

# 그리고 import area 뒤에 as ar을 붙여주면,
'''
import area as ar
print(dir())
'''
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'ar']
# 이번엔 ar이라고 나온다.

# area 모듈들의 함수를 직접 가져와보자.

from mymath.shapes import circle, sphere
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'circle', 'square']
# 이번에는 area는 나오지 않고 circle이나 square만 나온다.


# 이걸 이용하면 프로그램에서 사용되는 이름들을 좀 더 쉽게 관리할 수 있다.