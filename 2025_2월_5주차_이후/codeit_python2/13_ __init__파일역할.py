# __init__파일은 간단히 말해서 이 폴더는 파이썬 패키지다. 라고 말해주는 파일이다.
# initialize 라는 단어의 준말임. (= 초기화)
# 만약 사용자가 처음으로 패키지나, 패키지 안에 있는 어떤 것을 임포트하면, 가장 먼저 이 init 파일에 있는 코드가 실행된다는 뜻이다.

# 현재 shapes 패키지 내 __init__ 파일에 명령어를 넣어 둔 상태다 shapes를 임포트 해보자.

import mymath.shapes.area
# __init__파일 실행
# 실행 결과로 __init__파일 내에 있는 명령어가 실행됐다.

# shapes 내 모듈도 불러보자.

import mymath.shapes.volume


print(mymath.shapes.volume.cube(2))

# __init__파일 실행
# 8
# 무조건 처음으로 __init__파일이 실행되고 그 다음 volume 내 함수인 cube가 실행되었다.