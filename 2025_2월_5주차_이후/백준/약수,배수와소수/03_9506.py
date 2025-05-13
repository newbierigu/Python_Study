# 문제
# 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다.
# 예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.
# n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

# 입력
# 입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100,000)
# 입력의 마지막엔 -1이 주어진다.

# 출력
# 테스트케이스 마다 한줄에 하나씩 출력해야 한다.
# n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).
# 이때, 약수들은 오름차순으로 나열해야 한다.
# n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.


'''풀이 과정
-1 입력으로 프로그램 종료

for i in range(1, n + 1)
n % i 로 약수 구함
그 약수들의 합 확인 n 제외

sum_약수 == n 일 시 공식 오름차순으로 출력
아니면 아닌걸로 출력
'''




while True:
    sum_num = 0
    num = []
    n = int(input())
    if n == -1:
        break

    for i in range(1, n):
        if n % i == 0:
            num.append(str(i))
            sum_num += i


    if sum_num == n:
        print(f"{n} = {' + '.join(num)}")     # 리스트의 요소를 ' + '로 연결하여 출력
        continue

    else:
        print(f"{n} is NOT perfect.")
        continue