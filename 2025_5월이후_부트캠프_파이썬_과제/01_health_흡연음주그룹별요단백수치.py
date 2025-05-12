import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter # PercentFormatter는 y축(또는 x축) 숫자들을 퍼센트(%) 형태로 표시해주는 도구

# 비교용 데이터프레임
# '그룹', '요단백_이상 비율' 키에 나머지 벨류들이 들어감(딕셔너리)
data = pd.DataFrame({
    '그룹': ['흡연/음주,비음주', 
           '음주/흡연,비흡연', 
           '비흡연/음주,비음주', 
           '비음주/흡연,비흡연'],
   
    '요단백_이상 비율': [0.0124, 
                  0.009, 
                  0.0093, 
                  0.0117]
})

# barplot 색상 설정
# color_map 변수를 생성하여 "문자열(그룹명) : 색상 코드" 를 연결했음(딕셔너리)
color_map = {
    '흡연/음주,비음주' : '#1f77b4',
    '음주/흡연,비흡연' : '#1f77b4',
    '비흡연/음주,비음주' : '#fa8072',
    '비음주/흡연,비흡연' : '#fa8072'

}
# 리스트 컴프리헨션을 사용하여 색상 리스트 만듬
colors = [color_map[group] for group in data['그룹']]


# 그래프 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'

# 그래프 사이즈
plt.figure(figsize=(12, 6))

# 그래프 생성
sns.barplot(data=data, x='그룹', y='요단백_이상 비율', palette=colors, width=0.6)

# y축의 숫자 포맷을 퍼센트(%)로 변경한다.
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))

# y축 표시 범위 0 ~ 1.5 % 까지 
plt.ylim(0, 0.015) 

# 그래프 제목목과 x, y 축 제목 설정
plt.title('흡연/음주 상태별 요단백 이상 비율 비교')
plt.ylabel('요단백_이상 비율')
plt.xlabel('그룹')

# 그래프 안의 요소들이 서로 겹치지 않게 자동으로 레이아웃을 조정하는 명령어
plt.tight_layout()  

plt.show()