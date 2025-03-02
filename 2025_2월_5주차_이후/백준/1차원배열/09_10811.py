# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 순서대로 적혀져 있다. 
# 바구니는 일렬로 놓여져 있고, 가장 왼쪽 바구니를 1번째 바구니, 그 다음 바구니를 2번째 바구니, ..., 가장 오른쪽 바구니를 N번째 바구니라고 부른다. 
# 도현이는 앞으로 M번 바구니의 순서를 역순으로 만들려고 한다. 
# 도현이는 한 번 순서를 역순으로 바꿀 때, 순서를 역순으로 만들 범위를 정하고, 그 범위에 들어있는 바구니의 순서를 역순으로 만든다.
# 바구니의 순서를 어떻게 바꿀지 주어졌을 때, 
# M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 
# 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

# 출력
# 모든 순서를 바꾼 다음에, 가장 왼쪽에 있는 바구니부터 바구니에 적혀있는 순서를 공백으로 구분해 출력한다.


'''풀이 과정
문제를 이해해보자
총 N개의 바구니가 있으면 M번 바꿀 기회를 정함
i 와 j는 순서를 역순으로 바꿀 범위를 정함
i 부터 j 까지는 무조건 역순으로 바뀜
이걸 코드로 짜보자
'''

basket = []                             # 리스트화 하여 진행하기 위해 basket list 생성


N, M = map(int, input().split())        # 총 바구니 개수 N 과 바꿀 기회 M 입력 값 자리 생성

for a in range(N):                      # 총 바구니 개수 만드는 코드 생성
    a += 1
    basket += [a]

for _ in range(M):                      # 역순으로 바꿔주는 코드 생성
    i, j = map(int, input().split())    # i 부터 j 까지 범위 입력 값 자리 생성
    basket_rev = basket[i - 1 : j]      # 슬라이싱은 원본 리스트의 복사본 변환이어서 원본 리스트 영향을 주지 않음
    basket_rev.reverse()                # 새로운 변수 basket_rev를 생성하여 list 함수인 reverse를 사용용
    basket[i - 1 : j] = basket_rev      # 설정된 범위 자리에 역순으로 변환된 basket_rev 로 채움

def basket_answer():                    # 리스트 벗겨주는 함수 생성
    result = ''
    for num in basket:                  # result 에 basket 요소 값 하나씩 대입하기
        result += str(num) + ' '        # 공백으로 분리하기위해 ' ' 끝에 더해줌줌
    return result

print(basket_answer())                  # 정답




'''다음번엔 이렇게 풀어보자
N, M = map(int, input().split())  # 바구니 개수 N과 역순 변경 횟수 M 입력

basket = list(range(1, N + 1))  # 1부터 N까지 숫자가 들어간 리스트 생성

for _ in range(M):
    i, j = map(int, input().split())  # 범위 입력받기
    basket[i - 1:j] = reversed(basket[i - 1:j])  # 슬라이싱 후 역순 변경

print(*basket)  # 리스트의 요소를 공백으로 구분해 출력
'''
