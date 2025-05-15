len_array = int(input())
array = []

for i in range(1, len_array + 1):  # 길이에 맞는 수열 준비
    array.append(i)

Final_array = list(map(int, input().split())) # 최종 수열

rotation_ranges = []
in_rotation = False                 # 지금 회전 중인 구간 안에 있는지 표시
start = 0

for i in range(len(Final_array)):
    if Final_array[i] < 0:
        if not in_rotation:
            start = i               # 회전 구간의 시작
            in_rotation = True

    else:
        if in_rotation:
            end = i                 # 회전 구간의 끝
            rotation_ranges.append((start + 1, end + 1)) # 인덱스
            in_rotation = False

if in_rotation:
    rotation_ranges.append((start + 1, len(Final_array)))  # 음수가 끝날 경우 마지막 구간 추가

for r in rotation_ranges:
    print(f"{r[0]} {r[1]}")