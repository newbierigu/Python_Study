import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

# ——————————————————————————————————————————————
# 1) 한글 폰트 로드 및 seaborn 테마 설정
# ——————————————————————————————————————————————

# Windows 기본 폰트 중 '맑은 고딕' 파일 경로 지정
font_path = 'C:/Windows/Fonts/malgun.ttf'

# FontProperties를 통해 진짜 폰트 이름을 얻어낸 뒤
font_name = fm.FontProperties(fname=font_path).get_name()

# seaborn 테마를 깔끔한 'white' 스타일로 설정하면서
# 전체 그림 크기와 한글 폰트를 한 번에 지정
sns.set_theme(
    style='white',
    rc={
        'figure.figsize': (10,5),       # 그림 크기: 가로 10인치, 세로 5인치
        'font.family': font_name,       # 맑은 고딕
        'axes.unicode_minus': False     # 음수 부호가 깨지지 않도록
    }
)



# ——————————————————————————————————————————————
# 2) 데이터 불러오기 및 그룹화
# ——————————————————————————————————————————————

# CSV 파일을 pandas DataFrame으로 읽어옴
df = pd.read_csv(
    'C:/Users/nuwba/Desktop/과제/파이썬용csv/요단백_체중_연령대코드.csv'
)

# 체중과 연령대코드의 조합별로 '요단백' 컬럼(0/1) 의 평균을 구하면
# 1(단백뇨 양성)이 나온 비율이 되므로, mean()을 쓴다.
grouped = (
    df
    .groupby(['체중', '연령대코드'])['요단백']  # ➔ (체중, 연령대코드)별로 그룹화
    .mean()                                   # ➔ 그룹별 요단백 평균(1이 나온 비율)
    .reset_index(name='요단백_평균')           # ➔ 결과를 세로 형태의 DataFrame으로 복원
)



# ——————————————————————————————————————————————
# 3) Scatter plot 그리기
# ——————————————————————————————————————————————

fig, ax = plt.subplots()

# 1) x: 체중, y: 연령대코드
# 2) 색상(c)에는 '요단백_평균'의 4제곱근 (np.sqrt(np.sqrt(...)))을 줘서
#    값 차이를 부드럽게 강조/완화했습니다.
# 3) cmap='coolwarm' 으로 낮은 값 파랑→높은 값 빨강
# 4) edgecolor과 linewidth로 점 테두리를 살짝 넣어 가독성 ↑
sc = ax.scatter(
    x = grouped['체중'],
    y = grouped['연령대코드'],
    c = np.sqrt(np.sqrt(grouped['요단백_평균'])),
    cmap = 'coolwarm',
    s = 50,
    edgecolor = 'k',
    linewidth = 0.3
)


# ——————————————————————————————————————————————
# 4) 축 이름과 제목 한글로 설정
# ——————————————————————————————————————————————

ax.set_xlabel('체중 (kg)')                     # X축 레이블
ax.set_ylabel('연령대코드')                     # Y축 레이블
ax.set_title('체중/연령대 기준 요단백 수치 비율')  # 전체 제목


# ——————————————————————————————————————————————
# 5) 오른쪽에 colorbar(색 범례) 추가
# ——————————————————————————————————————————————

cbar = fig.colorbar(sc, ax=ax)
cbar.set_label('요단백=1 비율')  # 범례 제목



# ——————————————————————————————————————————————
# 6) 레이아웃 정리 및 출력
# ——————————————————————————————————————————————

plt.tight_layout()  # 여백 자동 조정
plt.show()         # 화면에 보여주기