# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 
# 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.
# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.
# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.


# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 
# 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 교환한다.

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.

'''풀이 과정
1. 바구니 N개 / 공 변경 기회 M
2. 처음 바구니에는 바구니와 같은 번호의 공이 들어있음
3. 바구니 2개를 선택하여 공을 서로 교환
4. 입력 첫 줄에 N M 공백으로 구분되어 입력됨
5. 입력 둘째 줄 부터 i번 바구니와 j번 바구니를 공백으로 구분되어 입력
6. 최종적으로 바구니 안에 있는 공의 번호를 순서대로 공백자로 구분하여 출력

만약 N = 5 M = 3 이면
1 2 3 4 5
에서 3번 공을 바꿀 기회가 주어지고 여기서 i j 를
3 4     3번 4번 위치 변경 > 1 2 4 3 5
1 2     1번 2번 위치 변경 > 2 1 4 3 5
4 4     4번 위치 그대로   > 2 1 4 3 5

2 1 4 3 5 로 출력되야함
'''

N ,M = map(int,input().split())                                          # 바구니 개수 / 공 변경 횟수 입력 값 만들기
basket = []

for balls in range(1, N + 1):                                            # 바구니 만들기
    basket += [balls]

for _ in range(M):
    i ,j = map(int,input().split())                                      # 공 교환되는 번호 만들기
    basket[i - 1], basket[j - 1] = basket[j - 1], basket[i - 1]


def answer(basket):                                                      # 리스트 벗겨주기
    result = ""
    for i in basket:
        result += str(i) + ' '
    
    return result

print(answer(basket))

# 개선할 점

# 1. 현재는 basket += [balls]를 사용했지만, 리스트 컴프리헨션을 활용하면 더 깔끔해 짐
# 39번 줄 : basket += [balls] >> basket = [i for i in range(1, N + 1)]
# 39번 줄 : basket += [balls] >> basket = list(range(1, N + 1)) 단순하게 표현하는것도 좋은 방법

# 2. 현재 answer 함수는 문자열을 += 연산으로 계속 더하는 방식인데, 파이썬에서는 리스트를 join()으로 합치는 게 훨씬 빠름
# 49번 줄 : result += str(i) + ' ' 
# >> def answer(basket):
#        return " ".join(map(str, basket))  리스트를 문자열로 변환 후 join()

# 이렇게 하면 연결 연산자(+=)를 사용한 반복문 보다 성능이 훨씬 좋음