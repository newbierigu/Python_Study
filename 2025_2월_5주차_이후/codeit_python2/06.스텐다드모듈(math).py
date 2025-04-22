# 스탠다드 모듈이란 : 파이썬을 설치할 때 기본적으로 들어있는 모듈들
# 스탠다드 모듈을 사용해보자.
# math : 여러가지 수학관련 함수들을 담고있는 모듈

import math

print(math.log10()) # 로그 함수를 사용하고 싶을 때
print(math.cos())   # 코싸인 함수를 사용하고 싶을 때


# math 모듈에 있는 특정 함수들만 사용하고 싶을 땐?

from math import log10, cos

# 이런식으로 사용할 수 있다.
