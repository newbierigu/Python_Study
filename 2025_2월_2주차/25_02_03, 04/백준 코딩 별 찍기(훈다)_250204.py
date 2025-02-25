# 백준 코딩 별 찍기
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, n 번째 줄에는 별 n 개를 찍는 문제
# 첫째 줄에 N(1<= N <= 100) 이 주어진다.
# 첫째 줄부터 N 번째 까지 차례대로 별을 출력한다.

# 정답 1
star = 0
n = int(input())

for star in range(1, n + 1):
    print('*' * star, end = " ")
    print()


# 정답 2
star = 0 

while True:
    i = int(input())
    for star in range(1, i + 1):
        print('*' * star)
    break
