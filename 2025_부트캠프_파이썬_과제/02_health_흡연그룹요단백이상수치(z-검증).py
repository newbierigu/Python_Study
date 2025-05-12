import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from matplotlib.ticker import PercentFormatter

# 1. 데이터 불러오기: CSV 파일 경로를 실제 위치로 바꿔주세요.
df = pd.read_csv('C:/Users/nuwba/Desktop/과제/파이썬용csv/흡연_요단백이상수치.csv')

# 그룹별 집계
# 2. 흡연 여부별로 '이상(1)' 개수와 전체 샘플 수 계산
grouped = df.groupby('흡연(비흡연(0) / 흡연(1))')['요단백(정상(0) / 이상(1)']
counts = grouped.sum().values    # 비흡연에서 요단백이 1인 데이터 개수 / 흡연에서 요단백이 1인 데이터 개수 
nobs  = grouped.count().values   # 비흡연 총 개수/ 흡연 총 개수


# 3. 각 그룹의 비율과 전체 합동 비율 구하기
p_smoker     = counts[1] / nobs[1]           # 흡연 그룹의 이상 비율
p_non_smoker = counts[0] / nobs[0]           # 비흡연 그룹의 이상 비율
p_all     = counts.sum() / nobs.sum()        # 전체 합친 이상 비율


# 4. 표준오차 및 Z-통계량
se  = np.sqrt(p_all*(1-p_all)*(1/nobs[1] + 1/nobs[0])) # 표준 오차 값
z_stat = (p_smoker - p_non_smoker) / se                # z통계량 값 (비교 대상의 차이 / 표준편차)


# 5. 양측 검정 P-값 계산: 절대값을 사용해 양쪽 모두 고려
p_value = 2 * norm.sf(abs(z_stat))     # “관측된 z-값보다 더 극단적인 값이 우연히 나올 확률”

# abs(z_stat) → 양쪽 꼬리의 시작점
# norm.sf(...) → 한쪽 꼬리(오른쪽) 확률
# 2 * … → 위아래 양쪽 꼬리를 합산

# 6. 결과 출력 및 해석
alpha = 0.05    # 유의수준 5%


# print(f"비흡연 그룹 비율 : {p_non_smoker:.4f}") # 소수점에서 PercentFormatter 사용하여 %로 변경
print(f"비흡연 그룹 요단백 이상 비율 : {p_non_smoker:.2%}")
print(f"흡연 그룹 요단백 이상 비율   : {p_smoker:.2%}")
print(f"전체 합동 요단백 이상 이상 비율   : {p_all:.2%}")
print(f"Z-통계량    : {z_stat:.4f}")
print(f"P-값        : {p_value:.4f}")


if p_value < alpha:
    print(f"유의수준 {alpha:.2f}에서 귀무가설 기각 → 두 그룹 간 비율 차이가 통계적으로 유의합니다.")
else:
    print(f"유의수준 {alpha:.2f}에서 귀무가설 채택 → 두 그룹 간 비율 차이가 통계적으로 유의하지 않습니다.")


# 7. 바 그래프 형성
# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
# 그래프 사이즈 설정
plt.figure(figsize=(6, 4))

# seaborn으로 바 그래프 형성
sns.barplot(
    x=['비흡연자','흡연자'],            # x축 형성
    y=[p_non_smoker, p_smoker],       # y축 형성 (짝궁>> p_non_smoker : 비흡연자, p_smoker : 흡연자)
    palette=['#1f77b4', '#fa8072'],   # 바 색상 설정 (palette)
    width=0.4                         # 바 두께 설정(width)
)

plt.ylabel('요단백 이상 비율')
plt.ylim(0, max(p_smoker, p_non_smoker) * 1.2)             # y축 표시 범위를 ymin부터 ymax까지로 설정하는 함수 ex).(0부터, y축최댓값 * 여유공간 1.2)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0)) # y축의 눈금 레이블을 백분율(%)로 바꿔주는 역할
plt.title('흡연 여부별 요단백 이상 비율')

plt.tight_layout() # 그래프 비율 자동 정리
plt.show()
