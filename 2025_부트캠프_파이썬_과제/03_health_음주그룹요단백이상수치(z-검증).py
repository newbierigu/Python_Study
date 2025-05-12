import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from matplotlib.ticker import PercentFormatter


df = pd.read_csv("C:/Users/nuwba/Desktop/과제/파이썬용csv/음주_요단백이상수치.csv")

grouped = df.groupby('음주(비음주(0) / 음주(1))')['요단백(정상(0) / 이상(1))']
counts = grouped.sum().values    # 비음주에서 요단백이 1인 데이터 개수 / 음주에서 요단백이 1인 데이터 개수 
nobs  = grouped.count().values   # 비음주 총 개수/ 음주 총 개수

p_drinker     = counts[1] / nobs[1]             # 음주 그룹의 이상 비율
p_non_drinker = counts[0] / nobs[0]           # 비음주 그룹의 이상 비율
p_all     = counts.sum() / nobs.sum()         # 전체 합친 이상 비율


se  = np.sqrt(p_all*(1-p_all)*(1/nobs[1] + 1/nobs[0])) # 표준 오차 값
z_stat = (p_drinker - p_non_drinker) / se          # z통계량 값 (비교 대상의 차이 / 표준편차)


p_value = 2 * norm.sf(abs(z_stat))     # “관측된 z-값보다 더 극단적인 값이 우연히 나올 확률”
alpha = 0.05    # 유의수준 5%


print(f"비음주 그룹 요단백 이상 비율 : {p_non_drinker:.2%}")
print(f"음주 그룹 요단백 이상 비율   : {p_drinker:.2%}")
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
    x=['비음주자','음주자'],            # x축 형성
    y=[p_non_drinker, p_drinker],     # y축 형성 (짝궁>> p_non_drinker : 비음주자, p_drinker : 음주자)
    palette=['#1f77b4', '#fa8072'],   # 바 색상 설정 (palette)
    width=0.4                         # 바 두께 설정(width)
)

plt.ylabel('요단백 이상 비율')
plt.ylim(0, max(p_drinker, p_non_drinker) * 1.2)           # y축 표시 범위를 ymin부터 ymax까지로 설정하는 함수 ex).(0부터, y축최댓값 * 여유공간 1.2)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0)) # y축의 눈금 레이블을 백분율(%)로 바꿔주는 역할
plt.title('음주 여부별 요단백 이상 비율')

plt.tight_layout() # 그래프 비율 자동 정리
plt.show()