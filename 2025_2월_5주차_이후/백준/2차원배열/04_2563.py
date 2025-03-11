# 문제
# 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
# 이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
# 이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
# 예를 들어 흰색 도화지 위에 세 장의 검은색 색종이를 그림과 같은 모양으로 붙였다면 검은색 영역의 넓이는 260이 된다. (그림 참고 : https://www.acmicpc.net/problem/2563)

# 입력
# 첫째 줄에 색종이의 수가 주어진다. 
# 이어 둘째 줄부터 한 줄에 하나씩 색종이를 붙인 위치가 주어진다. 
# 색종이를 붙인 위치는 두 개의 자연수로 주어지는데 
# 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 
# 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리이다. 
# 색종이의 수는 100 이하이며, 색종이가 도화지 밖으로 나가는 경우는 없다

# 출력
# 첫째 줄에 색종이가 붙은 검은 영역의 넓이를 출력한다.

'''풀이 과정
첫 번째 입력 : 색종이 수
두 번째 입력 : 자연수 2개 
              첫 번째 자연수 = 도화지 왼쪽 변과 색종이 왼쪽 변 사이의 거리
              두 번째 자연수 = 도화지 아래쪽 변과 색종이 아래쪽 변 사이의 거리다.

도화지의 크기는 100 x 100
색종이의 크기는 10 x 10

ex)
색종이 수 = 3

색종이 위치
첫 번째 색종이 = 3 7
두 번째 색종이 = 15 7
세 번째 색종이 = 5 2

첫 번째 색종이 오른쪽 변 위치 = 3 + 10 (13)
              위쪽 변 위치  = 7 + 10 (17)

두 번째 색종이 오른쪽 변 위치 = 15 + 10 (25)
              위쪽 변 위치 = 7 + 10 (17)

세 번째 색종이 오른쪽 변 위치 = 5 + 10 (15)
               위쪽 변 위치 = 2 + 10 (12)

겹치는 색종이

입력 값 내 왼쪽 변 위치 촤대 값 = 15
왼쪽 변 위치 최대 값 15 에서 색종이 크기 10 을 뺌
15 - 10 = 5
다른 색종이의 왼쪽 변 사이 거리가  5 보다 크면 겁치고 5보다 작거나 같으면 안겹침

입력 값 내 위쪽 변 최대 값 = 7
위쪽 변 위치 최대 값 7
최대 값이 색종이 크기 10 보다 작아서
어떻게든 겹침
그러나 왼쪽 변 위치 안겹친다면
무조건 안 겹침

현재 예시는 두 번째 색종이한테 겹치지 않음
하지만 첫 번째 색종이와 세 번째 색종이는 겹침

첫 번째 색종이 위치 = 왼쪽 3 오른쪽 13 아래 7 위 17
세 번째 색종이 위치 = 왼쪽 5 오른쪽 15 아래 2 위 12

가로 변 2 차이 세로 변 5 차이
색종이의 넓이 10 x 10

겹치는 부분 을 빼야 함

세 번째 왼쪽 - 첫 번째 오른쪽 = 8
첫 번째 아래 - 세 번째 위 = 5

겹치는 색종이 넓이 = 40
그럼 겹치는 색종이 중 한 색종이는 넓이 그대로 쓰고

나머지 색종이는 넓이에 겹치는 부분 - 해주면됨

색종이 2개 넓이 100 + 100 = 200

겹치는 색종이 계산한 나머지 색종이 넓이 100 - 40 = 60

총 260 이 나옴
'''







"""위 풀이 과정의 좋은 점 과 보완 점

좋은 점
1 도화지 크기와 색종이 크기를 명확하게 이해하고 있음.
2 색종이의 위치를 기반으로 겹침 여부를 판단하려고 함.
3 겹치는 영역을 빼주는 방식으로 전체 넓이를 구하려는 시도가 있음.


보완할 점
1 겹침 판단 로직이 부정확함
  단순히 "왼쪽 변 위치의 최대값에서 10을 뺀 값"으로 겹침을 판단하는 것은 부정확해.
  실제로 겹치는지 확인하려면, 두 개의 사각형이 겹치는 조건을 따져야 함

  사각형 A(왼쪽: x1, 아래쪽: y1) / 사각형 B(왼쪽: x2, 아래쪽: y2)
    가로 방향 겹침 = x1 + 10 > x2 그리고 x2 + 10 > x1
    세로 방향 겹침 = y1 + 10 > y2 그리고 y2 + 10 > y1
    위 두 조건을 동시에 만족해야 실제로 겹치는 것

2 겹친 영역 넓이 계산이 부족함
  겹치는 면적이 40이라고 판단하는 방식이 보편적으로 적용될 수 없음
  겹치는 영역의 너비 = min(x1 + 10, x2 + 10) - max(x1,x2)
  겹치는 영역의 높이 = min(y1 + 10, y2 + 10) - max(y1,y2)
  이렇게 구해서 겹치는 넓이 = 너비 x 높이로 계산해야 함

3 겹치는 부분을 한 번만 고려하는 문제

  색종이가 3장 이상이면, 두 장이 아니라 여러 장이 겹칠 수도 있음.
  지금 방식대로 하면 한 쌍의 색종이끼리만 계산하니까, 3장 이상이 겹칠 때 중복된 계산을 못 잡아냄.
  보통 2차원 배열(100x100 도화지)를 사용해서 채우는 방식이 더 직관적이고 정확할 수 있음.
"""


# 100x100 크기의 도화지를 0으로 초기화
dohwaji = [[0] * 100 for _ in range(100)]

# 색종이 개수 입력
n = int(input())

# 색종이 붙이기
for _ in range(n):
    x, y = map(int, input().split())  # 색종이의 왼쪽 아래 좌표
    
    # 10x10 영역을 1로 채우기
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            dohwaji[i][j] = 1

# 색종이가 붙은 영역(1의 개수) 계산
area = sum(sum(row) for row in dohwaji)
print(area)