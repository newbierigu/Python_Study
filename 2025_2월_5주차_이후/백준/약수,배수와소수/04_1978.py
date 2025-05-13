# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.






# math 함수 가져옴
import math
# math.sqrt(x) 사용을 위해 가져옴(math.sqrt(x) : 인자의 제곱근을 소수로 반환한다.)
# ex) math.sqrt(5) # 2.23606797749979

# math.isqrt(x) : 인자의 제곱근을 소수점 내림하여 정수로 반환한다. (3.8부터 사용 가능)
# math.isqrt(5) # 2

# ※ 음의 값을 인자로하면 ValueError가 발생한다.


# 입력할 변수 창조
N = int(input())
num = list(map(int, input().split()))
num_count = 0

# 입력한 수 중 소수 판별
for x in num:
    if x < 2:                                   # 숫자 1 은 넘김
        continue
    is_prime = True                             # 소수인지 확인하는 변수
    for i in range(2, int(math.sqrt(x)) + 1):   # 입력한 숫자를 범위로 잡고 2 부터 입력한 숫자 까지 하나 씩 나눠봄
        if x % i == 0:
            is_prime = False                    # 만약 2 부터 나누다 본인 숫자 빼고 나눠진다면 소수가 아님.
            break                               # 소수가 아님이 판별 났으므로 다음 숫자로 넘어감 이 숫자는 더 이상 검사할 필요 없음
    if is_prime:                                # is_prime 이 True 유지 되면, (소수라서 위 공식에서 False로 바뀌지 않음)
        num_count += 1                          # 소수일 때만 증가

print(num_count) 