# 패키지 폴더 내에 있는 모듈을 임포트하려면, 아래와 같이 사용하면된다.
'''
import shapes.volume

'''



# 그리고 그 안의 모듈을 사용하려면,
'''
print(shapes.volume.cube(3)) # 정육면체의 부피
'''
# 27
# 이렇게 사용하면 된다.





# 여기서도 as 사용이 가능하다.
'''
import shapes.volume as vol

print(vol.cube(3)) # 정육면체의 부피
'''
# 27
# 정상적으로 사용된다.




# from 사용도 가능하다.
'''
from shapes import volume  # == import shapes.volume 과 같다. 다만 모듈 사용 시 (shapes.volume.) 이 아니라 (volume.) 이 된다.

print(volume.sphere(5)) # 구의 부피
'''
# 523.3333333333334
# 정상 출력된다.



# 이번에는 area에서 가져와보자.
'''
from shapes.area import circle, square

print(circle(5)) # 원의 넓이
'''
# area 모듈 이름: shapes.area
# 78.5

# area 모듈의 던더네임도 shapes.area로 변경되고,
# 결과 값도 잘 출력된다.



# 패키지 폴더 자체를 임포트 한다면 오류가 발생한다.
"""
import shapes

print(shapes.area.circle(2))
"""
# module 'shapes' has no attribute 'area' 오류 발생
"""
import shapes

print(shapes.volume.cube(2))
"""
# module 'shapes' has no attribute 'area' 오류 발생

# 패키지 안에 있는 모듈들도 같이 임포트 하려면 __init__ 파일을 사용 하면된다.