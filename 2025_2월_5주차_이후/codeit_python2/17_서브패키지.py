# 서브 패키지란?
# 패키지 안에 패키지 파일이 서브 패키지이다.

# 지금부터 이전까지 써온 shapes 패키지와
# 새로 만들 stats 패키지를
# mymath라는 패키지 안에 넣어줄것이다.

# stats 패키지 안에는 average와 spread 모듈이 있다.
# average : data_mean(데이터 평을 구해주는 함수) / deta_median (데이터 중앙 수를 구해주는 함수)
# spread : data_range (데이터 범위를 구해주는 함수)

# 이제 각 모듈 안 init 파일에 코드를 작성해보자.
# shapes_init 파일에는  from mymath.shapes import area, volume
# stats_init 파일에는 from mymath.stats import average, spread

# 그 다음 mymath 패키지 안 init 파일에도 적용시켜보자.
# from mymath.stats.average import data_mean # mymath 안에 stats 모듈에있는 average 함수에서 data_mean 함수를 가져오겠다. 라는 코드다.
"""
정리
from mymath.stats.average import data_mean # mymath 안에 stats 패키지에 있는 average 모듈에서 data_mean 함수를 가져오겠다.

# mymath 안에 stats 모듈에 있는 average 모듈의 모든 함수를 가져오겠다.
from mymath.stats import average # average.data_mean()
import mymath.stats.average # mymath.stats.average.data_mean()

# stats 전부 가져오기
from mymath import stats
import mymath.stats
"""


# 성공 감사합니다.