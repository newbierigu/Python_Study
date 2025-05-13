# 밑에 나와 있는 chicken.txt 파일을 보세요. 
# 제가 운영하는 치킨집 '코딩에빠진닭(이하 코빠닭)'의 12월 매출이 정리되어 있습니다.
# :의 왼쪽에는 해당 월의 며칠인지, 그리고 오른쪽에는 그 날의 매출이 적혀 있습니다.
# data 폴더의 chicken.txt 파일을 읽어 들이고, strip과 split을 써서 12월 코빠닭의 하루 평균 매출을 출력하세요. 
# 평균을 구하기 위해서는 총 매출을 총 일수로 나누면 됩니다. 
# 참고로 현재 제공된 파일에는 31일이 있지만, 어떤 달은 31일이 아닐 수도 있습니다. 
# 이 점을 고려해서 확장성 있는 코드를 작성해 주시길 바랍니다.

totla_slaes = 0
days_count = 0

with open("2025_2월_5주차_이후/codeit_python/data/chicken.txt", 'r', encoding='utf-8') as f:

    for line in f:
        data = line.strip()                 # 공백 제거
        days_sales = data.split(': ')       # 일/매출 나누기

        totla_slaes += int(days_sales[1])   # 하루 매출 값 뽑아서 달 값에 누적시키기
        days_count += 1                     # 월 평균을 내기 위한 일 수 세기

print(totla_slaes / days_count)             # 월 평균 매출