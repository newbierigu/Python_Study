# 문제
# X대학 M교수님은 프로그래밍 수업을 맡고 있다. 교실엔 학생이 30명이 있는데, 학생 명부엔 각 학생별로 1번부터 30번까지 출석번호가 붙어 있다.
# 교수님이 내준 특별과제를 28명이 제출했는데, 그 중에서 제출 안 한 학생 2명의 출석번호를 구하는 프로그램을 작성하시오.


# 입력
# 입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다. 출석번호에 중복은 없다.

# 출력
# 출력은 2줄이다. 1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력하고, 2번째 줄에선 그 다음 출석번호를 출력한다.

'''풀이 과정
문제 정리
1. 30 명의 학생 중 28명의 학생만 출석한 상태
2. 출석하지 않은 2명의 학생의 번호를 출력하는 코드 작성
3. 입력 28번 출력 2줄(작은 번호부터)
'''
'''
students = []                            # 리스트 화 시켜서 풀기
atd_students = []


for i in range(30):                      # 총 학생의 수
    students += [i + 1]                  

for _ in range(28):                      # 출석한 학생의 수
     students_num = int(input())
     atd_students += [students_num]      

def absent_students():                   # 결석한 학생 번호 거르기기
    result = []
    for student in students:
        if student not in atd_students:
            result.append(student)
    
    if result[0] < result[1]:
        print(result[0])
        print(result[1])
    else:
        print(result[1])
        print(result[0])
    
    return result

absent_students()
'''


# 다음에는 이렇게 생각해보자

students = set(range(1, 31))            # 총 학생 수

for _ in range(28):                     # 출석한 학생 수
    students.remove(int(input()))       # 입력한 학생을 총 학생 수에서 제거

missing = sorted(students)              # 남은 학생 수 번호 순으로 정렬
print(missing[0])                       # 순서대로 출력하기
print(missing[1])








