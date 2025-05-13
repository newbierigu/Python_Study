# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

'''풀이 과정
그룹 단어는 처음 나온 알파벳이 연속되서 같은 알파벳이 나오는 것 제외 나온 이후 같은 알파벳이 나오지 않는 것을 의미 함.
abc      =    그룹 단어
aabbcc   =    그룹 단어
abcaad  !=    그룹 단어

1. 그룹 단어의 수를 담을 변수 창조

   group_word = 0

2. 첫 입력 값으로 test case 가 주어짐
   tast case 만큼 단어를 입력 함

   test_case = int(input())
   for _ in range(test_case):
       word = input()

3. 저기서 word에 받아지는 단어를 확인하여
   if word == 그룹 단어면
   group_word += 1
   else:      아니면
       continue

4. 최종적으로 group_word 를 출력해주면 됨.

   print(group_word)

   
여기서의 문제는 3번 과정에서 word에 받아지는 단어가 그룹단어인지 아닌지를
판별하는 코드를 만드는 것이 문제.


1.  visited 라는 set 집합(중복 거름) 변수를 만들어주고
    prev 라는 직전 문자를 저장할 변수를 만들자

    visited = set() 


2. 그 다음 word의 문자를 가지고 연속이 유지되는지 확인 
   여기서의 연속은 abc 연속 abca a가 다시 나와서 연속 끊김

    for s in word:
        visited.add(s)
        prev = 

    # 현재 문자 s가 기존 문자 visited 안에 없는 새로운 문자 s not in visited
    # 직전 문자 prev 가 현재 문자와 다를 때 prev != s
    # 그룹 문자임
    
        if prev != s and s not in visited:
            group_word += 1

    # 현재 문자 s 가 기존 문자 visited 안에 들어있는 문자임 s in visited
    # 직전 문자 prev 가 현재 문자와 같을 때 prev == s
    # 그룹 문자임

        if prev == s and s in visited:
            group_word += 1

    # 그 외의 경우는 그룹 문자 아님
        else:
            group_word += 0

4. grop_word 값 출력
   print(group_word)


합쳐보자

위 내용 다 틀림 아래에서 다시 품

'''

group_word = 0

test_case = int(input())

for _ in range(test_case):
    word = input()

    visited = set()
    prev = ''

    ''' 
    for i, s in enumerate(word):        # enumerate 함수로 word 의 인덱스 번호 i와 문자 s를 가져옴

        if prev == s:                   # 첫 번째 조건
            if len(word) - 1 == i:      # 첫 번째 조건 내에서 word의 마지막 문자일 때
                group_word += 1         # group_word 에 +1 해주고 반복문 탈출
                break
            continue                    # 첫 번째 조건 prev(직전 문자) == s(현재 문자) 일 때 continue(다음 문자로 넘어 감)
                                        # 이 아래 줄 부터 싹 다 prev != s 이다.
        if s in visited:                # s가 visited 안에 존재한다면 prev != s 인데 이미나온문자(visited) 에 있다면 연속된 문자가 아님
            break                       # group_word 가 아니므로 반복문 탈출

        if len(word) - 1 == i:          # 첫 번째/두 번째 조건 통과 후 마지막 문자일 때
            group_word += 1             # 해당 단어 전부 검수한 후 그룹 단어인지 파악했으니 group_word 에 + 1 을 한다.

        visited.add(s)                  # visited (set 집합) 에 s를 추가해서 다음 반복 때 유니크성 체크
        prev = s                        # prev 가 직전 문자가 되기 위해 반복문 마지막으로 옴  
                                        # 마지막으로 넣었던 s가(= prev) 다음 반복 s와 만남
    '''

# 방법 2
    '''
    is_group_word = True                # is_group_word 라는 변수 생성 이 변수는 True로 설정해논 상태

    for s in word:                      # 똑같이 word 한 문자 씩 반복

        if prev == s:                   # 첫 번째 조건은 방법 1 첫번째 조건과 같이 직전 문자가 현재 문자와 같으면
            continue                    # continue 로 다음 문자로 넘어감
        
        if s in visited:                # 두 번째 조건은 현재 문자가 visited 안에 있을 때 (prev != s 인 상태)
            is_group_word = False       # visited는 이미 나왔던 문자들의 집합인데 s가 visited 안에 있다면 그룹 단어가 아님.
            break                       # 그러므로 is_group_word를 False로 바꾸고 반복문 탈출

        visited.add(s)                  # visited (set 집합) 에 s를 추가해서 다음 반복 때 유니크성 체크
        prev = s                        # prev 가 직전 문자가 되기 위해 반복문 마지막으로 옴  
                                        # 마지막으로 넣었던 s가(= prev) 다음 반복 s와 만남
    if is_group_word:
        group_word += 1                 # 반복문 끝났을 때 is_group_word 가 True면 group_word += 1 아니면 실행 안함.
    '''

# 방법 3

    group_word += 1                     # 일단 group_word += 1을 먼저 함

    for s in word:                      # word 내 문자 요소 하나씩 반복

        if prev == s:                   # 직전 문자와 현재 문자가 같으면면
            continue                    # 다음 word 문자요소 반복

        if s in visited:                # prev != s 일때 s가 visited 안에 들어가 있으면 
            group_word -= 1             # 만약 입력으로 aabbccaa 를 입력했으면, aa > bb > cc > (aa)여기서 a 가 이미 visited 안에 있어서
            break                       # 그룹 단어가 아님 group_word -= 1 을 하고 반복문 탈출
                                        # 이 조건은 바로 break가 실행되서 무조건 한번만 실행됨 

        visited.add(s)                  # visited (set 집합) 에 s를 추가해서 다음 반복 때 유니크성 체크
        prev = s                        # prev 가 직전 문자가 되기 위해 반복문 마지막으로 옴  
                                        # 마지막으로 넣었던 s가(= prev) 다음 반복 s와 만남
print(group_word)