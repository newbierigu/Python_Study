# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
# S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

'''풀이 과정
문제 이해
문제가 뭔가 어렵게 되어있는데
입 출력 예시가 나와서 쉽게 이해가 됨

첫 번째 입력 때 Tast Case = T가 주어짐
두 번째 입력 부터 (R 임의의 문장) 으로 입력됨
R = 각 문자가 반복되는 횟수
S = 반복할 문자
S가 ABC 이고 R이 3이면 AAABBBCCC로 공백없이 출력
'''

T = int(input())                 # Test Case 횟수 입력 받을 변수 생성


for _ in range(T):               # Test Case 만큼 반복할 반복문 생성
    answer = ''                  # 출력한 다음 다른 문장들과 섞이지 않기 위해 정답 변수 여기에 생성
    R, S = input().split()       # 문자가 반복할 횟수 R 과 반복될 문자 S 입력될 자리 생성
    R = int(R)                   # R int화
    S_range = len(S)             # S 문자의 범위 측정 코드 생성

    for i in range(0, S_range):  # i 에 S문장의 길이 만큼의 범위만큼 반복하는 코드 생성
        for _ in range(R):       # 문자 반복되게 만드는 R반복 생성
            answer += S[i]       # S문장의 인덱스 자리 i를 누적시켜 answer 코드에 저장

    print(answer)                # answer 출력




