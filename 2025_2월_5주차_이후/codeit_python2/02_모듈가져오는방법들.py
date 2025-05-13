# 만약 area 모듈에 circle 함수만 사용하고 싶다면, 
# area 모듈에서 circle 함수만 가져와라란 뜻으로


# 1. from 사용
'''
from area import circle     # 이런 식으로 사용할 수 있다.

print(circle(3))            # 이제 area. 이렇게 부를 필요 없이 circle()만 사용해도 된다.
'''

# 2. as 사용
'''
# 모듈 이름이 너무 길어서 줄여 사용하고 싶다면, as 를 사용하면 된다.

import area as ar

print(ar.circle(3))

'''
# 모듈 내 함수에도 적용 가능하다.
"""
from area import square as sq

print(sq(4))
"""

# 3. * 사용
# "from '모듈' import *" <<< *은 모듈 내 모든 함수를 가져오겠다는 뜻이다. square() circle()
# 다만 이렇게 쓰지 않는걸 추천한다. 어떤 이름의 함수가 어떤 모듈에서 왔는지 정확히 알 수가 없고
# 자기도 모르게 쓸 때 없는 것을 가져올 수가 있어서 이 방법은 추천하지 않는다.
"""
from area import *

print(square(4))
print(circle(3))
"""