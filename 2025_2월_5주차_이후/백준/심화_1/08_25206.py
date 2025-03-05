# 문제
# 인하대학교 컴퓨터공학과를 졸업하기 위해서는, 전공평점이 3.3 이상이거나 졸업고사를 통과해야 한다. 
# 그런데 아뿔싸, 치훈이는 깜빡하고 졸업고사를 응시하지 않았다는 사실을 깨달았다!
# 치훈이의 전공평점을 계산해주는 프로그램을 작성해보자.
# 전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
# 인하대학교 컴퓨터공학과의 등급에 따른 과목평점은 다음 표와 같다.
# A+	4.5
# A0	4.0
# B+	3.5
# B0	3.0
# C+	2.5
# C0	2.0
# D+	1.5
# D0	1.0
# F	0.0
# P/F 과목의 경우 등급이 P또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
# 과연 치훈이는 무사히 졸업할 수 있을까?

# 입력
# 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.

# 출력
# 치훈이의 전공평점을 출력한다.
# 정답과의 절대오차 또는 상대오차가 
# \(10^{-4}\) 이하이면 정답으로 인정한다.

# 제한
# 1 ≤ 과목명의 길이 ≤ 50
# 과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
# 학점은 1.0,2.0,3.0,4.0중 하나이다.
# 등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
# 적어도 한 과목은 등급이 P가 아님이 보장된다.


'''풀이 과정
과목명 학점 등급 입력 자리 만들자
20번 반복

subject_rating = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
subject_type = 20
score_sum = 0
major = 0

for _ in range(subject_type):
    subject, score, rating = map(str,input().split())
    score = float(score)
    
자리는 만들어 졌고 
전공 평점은 전공 과목별 학점 * 과목평점 의 합을 학점의 총합으로 나눈 값이다.

학점을 따로 빼서 등급에 맞는 과목평점과 곱한 다음 score_sum에 더한다.
와중에 P인 과목은 계산에서 제외시킨다.

    if rating == 'P':       # P인 과목은 계산에서 제외시킨다.
        continue

나머지 계산해서 평균 구하고

마지막에 출력


    '''



'''
# 방법 1 
subject_rating = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
subject_type = 20
score_sum = 0
sub_score_sum = 0
major = 0

for _ in range(subject_type):
    subject, score, rating = map(str,input().split())
    score = float(score)

    if rating == 'P':                                # P인 과목은 계산에서 제외시킨다.
        continue
    
    score_sum += score

    if rating == 'A+':
        sub_score_sum += score * subject_rating[0]
    
    if rating == 'A0':
         sub_score_sum += score * subject_rating[1]
    
    if rating == 'B+':
         sub_score_sum += score * subject_rating[2]

    if rating == 'B0':
         sub_score_sum += score * subject_rating[3]         

    if rating == 'C+':
         sub_score_sum += score * subject_rating[4] 

    if rating == 'C0':
         sub_score_sum += score * subject_rating[5] 

    if rating == 'D+':
         sub_score_sum += score * subject_rating[6] 

    if rating == 'D0':
         sub_score_sum += score * subject_rating[7] 

    if rating == 'F':
         sub_score_sum += score * subject_rating[8] 

major = sub_score_sum / score_sum                           # sub_score_sum 학점 x 과목평점의 총합 / 학점의 총합합

print(major)                                                # 전공 평점 출력

'''


# 방법 2 (딕셔너리 활용)


sub_rating = { 'A+':4.5, 'A0':4.0,                             # 딕셔너리를 통해 가져옴
              'B+':3.5, 'B0':3.0,
              'C+':2.5, 'C0':2.0,
              'D+':1.5, 'D0':1.0,
              'F':0 }

total_score = 0
weighted_score = 0

for _ in range(20):
    subject, score, rating = input().split()
    score = float(score)

    if rating == 'P':
        continue
    
    total_score += score

    weighted_score += score * sub_rating.get(rating, 0.0)      # .get 함수를 사용하여 딕셔너리 활용

major_score = weighted_score / total_score                     # 학점 * 과목평점 / 학점 총합합

print(major_score)
