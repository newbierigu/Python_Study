# 보통 모듈 통째로 import 할 때 import * 을 사용했었는데,
# from shapes.area import * 이 코드는 area 모듈에 있는 모든 함수를 가져오라는 뜻이다.

# 이걸 패키지에 한번 적용시켜보자.
# from shapes import * 이건 shapes에 있는 모든 함수를 가져오라는 뜻
# dir() 함수는 현재 파일에서 정의된 모든 이름들을 불러오는 것.
# dir()로 확인해보자.
from mymath.shapes import *

print(dir())
# ['PI', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# import * 를 패키지에 적용하면, 그 안에 엤는 아무 모듈도 임포트 되지 않는다.
# 이걸 바꿔주려면 init파일에 코드를 추가해줘야한다.
# __all__ = ['area', 'volume']


# all이라는 특수 변수(__가 붙은 변수) 생성
# all은 import *를 했을 때 어떤 것들을 가져와야 하는지 정해주는 변수이다.
# 위 코드를 다시 실행하면, 
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__',
#  'area', 'volume']
# area 와 volume 이 추가된다.


# __all__은 모듈에도 사용 가능하다.
# area : __all__ = ['circle', 'PI']
# volume : __all__ = ['sphere', 'PI']
# 각 모듈에 저렇게 작성하면, import *을 사용했을 때 저것들 만 사용하겠다는 뜻이 된다.

from mymath.shapes.area import *

print(dir())
# ['PI', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 
# 'area', 'circle', 'volume']
# 이렇게 가져올 수 있다.

# 하지만 import * 는 여전히 사용하기 어렵기 때문에
# 네임스페이스를 완전히 이해하고 있을 때만 사용하자.
