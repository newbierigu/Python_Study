import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter # PercentFormatter는 y축(또는 x축) 숫자들을 퍼센트(%) 형태로 표시해주는 도구

# 비교용 데이터프레임
# '그룹', '요단백_이상 비율' 키에 나머지 벨류들이 들어감(딕셔너리)
data = pd.DataFrame({
    '그룹': ['음주_그룹', 
           '비음주_그룹'],
   
    '흡연자_비율': [0.2473, 0.0883]
})

# barplot 색상 설정
# color_map 변수를 생성하여 "문자열(그룹명) : 색상 코드" 를 연결했음(딕셔너리)
color_map = {
    '음주_그룹' : '#1f77b4',
    '비음주_그룹' : '#fa8072'
}
# 리스트 컴프리헨션을 사용하여 색상 리스트 만듬
colors = [color_map[group] for group in data['그룹']]

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8, 6))
sns.barplot(data=data, x='그룹', y='흡연자_비율', palette=colors, width=0.4)
plt.gca().yaxis.set_major_formatter(PercentFormatter(1.0))
plt.title('음주그룹 내 흡연자 수 비율')
plt.ylabel('흡연자 수 비율')
plt.xlabel('그룹')
plt.tight_layout()
plt.show()