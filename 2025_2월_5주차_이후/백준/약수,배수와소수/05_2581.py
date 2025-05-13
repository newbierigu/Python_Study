# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.


'''풀이 과정
입력 값 M 과 N
출력 값 M이상 N이하 리스트 내 소수 값의 합 and 최솟값
       or 소수 없을 땐 - 1'''


import math                             # 전 문제와 비슷하게 해결 가능능

n = int(input())
m = int(input())
num_list = []

for i in range(n, m + 1):               # n ~ m 범위를 설정해줌
    if i < 2:                           # 혹시 1 범위 잡으면 1은 넘기기
        continue

    num_bool = True                                 # 두 번째 for문에서 if 다음 else를 사용했더니, 소수가 아닌 숫자들도 리스트에 들어감

    for j in range(2, int(math.sqrt(i)) + 1):       # else: 문은 for 루프의 각 반복마다 실행되기 때문에,                                                   
        if i % j == 0:                              # 어떤 j 값에서는 i % j == 0이 아니라면 (i가 j로 나누어 떨어지지 않으면)
            num_bool = False                        # 즉시 num_list.append(i)가 실행됨.
            break                                   # for문을 탈출하기 위해 else 대신 True False 로 소수를 가려 냄
    
    if num_bool:                                    # 여기 까지 num bool 가 True 면 소수란 뜻 > num List에 추가
        num_list.append(i)

if sum(num_list) == 0:                  # 마지막에 만약 num list 가 비어있으면 -1 출력
    print(-1)

else:
    print(sum(num_list))                # 아니면 num list의 합과, 최솟값을 출력력
    print(min(num_list))
