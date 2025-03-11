# 문제
# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다. 이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다. N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 더한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.

'''풀이 과정
N = 줄 개수
M = 행 개수

3 3 입력하면
3 줄에 3 개씩 입력하면 됨

num_A = []
num_B = []
num_sum = []

N, M = map(int,input().split()))

# num_A 행렬 생성
for _ in range(N):
    num_A.append(list(map(int,input().split())))

# num_B 행렬 생성
for _ in range(N):
    num_B.append(list(map(int,input().split())))

# num_A 와 num_B 더해주기
for i in range(N):
    row = []
    for j in range(M):
        row.append(num_A[i][j] + num_B[i][j])
    num_sum.append(row)

# 결과 출력하기
for row in num_sum:
    print(" ".join(map(str, row)))

    
'''

num_A = []
num_B = []
num_sum = []

N, M = map(int,input().split())

# num_A 행렬 생성
for _ in range(N):
    num_A.append(list(map(int,input().split())))

# num_B 행렬 생성
for _ in range(N):
    num_B.append(list(map(int,input().split())))

# num_A 와 num_B 더해주기
for i in range(N):
    row = []
    for j in range(M):
        row.append(num_A[i][j] + num_B[i][j])
    num_sum.append(row)


# 결과 출력하기
for row in num_sum:
    print(" ".join(map(str, row)))
