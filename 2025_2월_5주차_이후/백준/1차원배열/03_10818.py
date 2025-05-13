# 문제
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
# 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.


N = int(input())                                        # N = 정수의 개수
N_type = map(int,input().split())                       # N_type = 정수의 종류(N 개수만큼)

N_type_sequence = list(N_type)                          # N_type의 리스트화

print(min(N_type_sequence), max(N_type_sequence))       # N_type_sequence 내 요소 최소 값 과 최대 값 출력


# 의문점 1 : N_type의 개수가 N을 넘어갔을 때의 조건이 왜 없는지