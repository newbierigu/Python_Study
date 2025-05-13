from mymath.shapes import circle, square

x = float(input('원의 반지름을 입력해주세요: '))
print(f"반지름이 {x}인 원의 면적은 {circle(x)}입니다.\n")

y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
print(f'변의 길이가 {y}인 정사각형의 면적은 {square(y)}입니다.')

# 위 코드를 실행하면 정상 실행된다.
# 이 파일은 실제로 프로그램을 작동시키는 코드를 담은 실행 용도의 파일이다.
# 이걸 스크립트 라고 한다.

# 모듈은 직접 실행하지 않고, 다른 파일로 가져와서 사용한다.

# 스크립트 = 현재 파일, 모듈 = area 파일