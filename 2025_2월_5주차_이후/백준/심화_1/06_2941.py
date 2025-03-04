#문제
# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 
# 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.

# 크로아티아 알파벳	변경
# č	  >   c=
# ć	  >   c-
# dž  >	  dz=
# đ	  >   d-
# lj  >   lj
# nj  >   nj
# š	  >   s=
# ž	  >   z=

# 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 
# 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 
# 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력
# 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

# 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.


'''풀이 과정
입력값이 여러 번 쓰인 c= ,c-, dz=, d-, lj, nj, s=, z= 뺀 나머지 알파벳들은 다 리턴 값 1개로 인식
위 문자들을 리턴 값 1로 만들어주고 요소값 한 개당 1값을 쥐어주면 문제 해결

3 글자인 dz= 부터 걸러주고
2 글자 싹 걸러주고
나머지 알파벳 수 세기
결국엔 2/3글자 짜리를 위에서도 말했듯 1개로 인식시키면 되니까
임의의 문자로 치환해서 1개로 만든 후
len으로 글자 수를 세면 정답 결과가 나옴
'''
# 방법 1 (replace 활용)
'''
word = input()

word = word.replace('dz=', '*')

croatia_1 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for s in croatia_1:
    word = word.replace(s, '*')

print(len(word))
'''

# 방법 2 (슬라이싱 활용)

croatia_a = 0
word = list(input())

del_list = []

for i in range(len(word) - 3):
    if ''.join(word[i : i + 3]) == 'dz=':
        croatia_a += 1
        del_list.append(i)

if del_list:
    for item in del_list.reverse():
        del word[item : item + 3]

del_list = []

for i in range(len(word) - 2):
    if ''.join(word[i : i + 2]) in {'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='}:
        croatia_a += 1
        del_list.append(i)
        
        
if del_list:
    print(del_list)
    for item in del_list.reverse():
        del word[item : item + 2]

print(len(word) + croatia_a)



