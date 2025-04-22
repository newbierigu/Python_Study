"""
# 공부 진도 15에 해당되는 코드(__init__)
from mymath.shapes import PI
"""
# 공부 진도 16에 해당되는 코드
__all__ = ['circle', 'PI']

# 공부 진도 10에 해당되는 코드
print(f'area 모듈 이름: {__name__}')


# area라는 모듈을 만들어보자.
# 여러 도형의 면적을 구해주는 함수를 모아놓은 모듈
# 원의 면적을 구해주는 함수/정사각형의 면적을 구해주는 함수

PI = 3.14

# 원의 면적을 구해주는 함수

def circle(radius):
    return PI * radius * radius


# 정사각형의 면적을 구해주는 함수

def square(length):
    return length * length

# 함수를 만들었으니 이제 다른 파일에서 사용해보자.


# 공부 진도 10에 해당되는 내용
# 모듈 내 함수들을 테스팅 하는 메인 함수들
def main():
                       
    # circle 함수 Test         
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)
    
    # square 함수 Test
    print(square(2) == 4)
    print(square(5) == 25)

if __name__ == '__main__':     # area 파일의 던더네임이 __main__ 일 때 란 뜻은 이 파일을 직접 실행시켰다는 뜻
    main()                     # 그러므로 직접 실행 됐을 때만 아래의 코드들이 실행된다.
                               # 이것이 모듈 내 코드들을 스크립트에서 실행 시키지 않게 하는 방법이다.