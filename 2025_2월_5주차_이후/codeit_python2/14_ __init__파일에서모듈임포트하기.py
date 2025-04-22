# 함수의 호출방식 변경하는 방법~!

'''
import shapes
이렇게 패키지만 불러온 상태에서

print(shapes.area.circle(3))
실행하면 오류가 발생했었는데

이번엔 __init__ 파일을 사용하여 오류를 없에보자.
'''

# 1. __init__ 파일은 이 폴더가 패키지야 라는 의미도 있지만, 패키지 내에서 제일 먼저 실행되는 파일이다.
# 2. 그러므로 __init__ 폴더에서 모듈들을 임포트 시키면 오류가 발생하지 않는 것이다.
# 3. __init__파일에 from shapes import area, volume을 작성 후 위 코드를 다시 실행해보자.
'''
import shapes    # 실행될 때 __init__ 부터 실행된다. (= from shapes import area, volume 가 실행된다.)

print(shapes.area.circle(3))
print(shapes.volume.cube(3))
'''
# 28.259999999999998
# 27
# 정상 작동되는 것을 확인할 수 있다.



# __init__ 파일에는 패키지 전체를 끌고 올 필요가 없다.
# 필요한 모듈만 고르거나 묶어서 가져올 수 있다.
# 위 코드를 init 파일 내에서 import area만 남기고 volume 을 지우면 오류가 난다.


# __init__ 파일을 만약 from shapes.area import circle, square 로 한다면,
'''
import shapes

print(shapes.circle(3))
print(shapes.square(3))
'''
# 28.259999999999998
# 9
# 모듈 호출을 shapes.circle/shapes.square 로 해야한다.