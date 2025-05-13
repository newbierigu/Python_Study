# 지금 shapes에 들어간 모듈들에 공통되는 변수 PI가 있다.
# 이걸 __init__파일에서 변수로 처리하고 한번에 사용해보자.
# 패키지 내 공통 변수들은 한 번만 정의되는 것이 좋다.

'''
1. shapes 패키지 폴더 내 __init__ 파일에
   PI = 3.14 변수를 정의한다.
   
2. area, volume 모듈에서 정의한 PI를 지워주고

3. 각 모듈들에게 PI를 불러올 "from shpaes import PI" 를 작성해준다.
'''
# 이제 실행해보면,

from mymath.shapes import area, volume

print(area.circle(3))
print(volume.cube(3))

# 28.259999999999998
# 27
# 정상 작동된다.


# 참고로 __init__파일에서 정의한 변수는 바깥파일에서도 사용할 수 있다.
'''
1. __init__파일에서 PI를 정의했다.
2. 현재 파일에서 PI를 사용하고 싶다.
'''
import mymath.shapes.area
print(mymath.shapes.area.PI)

# 이렇게 사용할 수 있거나,

from mymath.shapes.area import PI
print(PI)

# 이렇게도 사용 가능하다.

