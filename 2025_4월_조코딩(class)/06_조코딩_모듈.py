# 만들어논 mod2 를 불러와보자.
# mod3는 클래스와 상수변수, 함수가 포함되어 있다.
# mod3 는 현재 module이라는 디렉토리 안에 있다. 같은 폴더 안에 있는 모듈이 아니기 때문에 그냥 import 하면 오류가 발생한다.
# 이 때 sys 를 사용한다.
'''
import sys

sys.path.append("C:/Users/nuwba/Desktop/Python_Study/2025_4월_조코딩(class)/module")

import mod3

a = mod3.Math()
print(a.solv(5))
'''

from module.mod3 import Math

a = Math()
print(a.solv(5))
