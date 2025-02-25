# a 터렛 b 터렛
# c 적 위치

# a의 좌표 x1 y1
# b의 좌표 x2 y2

# a와 c 사이의 거리 r1
# b와 c 사이의 거리 r2

# 각 테스트 케이스마다 c가 있을 수 있는 위치 수를 출력함.
# 만약 무한대일 경우 -1 출력 함


# 두 원의 중심 사이 거리
# 두 원이 완전히 동일한 경우 (무한대)
# 외접 또는 내접 (접점 1개)
# 두 원이 서로 겹칠 때 (교점 2개)
# 두 원이 아예 만나지 않을 때 (교점 없음)
# 입력 예제
# 결과 출력

from math import sqrt

def find_intersection_points(x1, y1, r1, x2, y2, r2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)  

    
    if d == 0 and r1 == r2:
        return -1
    
    
    elif d == r1 + r2 or d == abs(r1 - r2):
        return 1

   
    elif abs(r1 - r2) < d < (r1 + r2):
        return 2

    
    else:
        return 0

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    print(find_intersection_points(x1, y1, r1, x2, y2, r2))