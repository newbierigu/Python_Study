# 문제
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

# 입력
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# 출력
# 직사각형의 네 번째 점의 좌표를 출력한다.

a = []
b = []

for _ in range(3):
    x, y = map(int,input().split())
    a.append(x)
    b.append(y)

from collections import Counter                         # Counter : 중복된 데이터가 저장된 배열을 인자로 넘기면 각 원소가 몇 번씩 나오는지가 저장된 객체를 얻게 됩니다.
                                                        # 1. 저장된 배열 = 리스트 내 요소
def unique_elements(a):                                 # 2. 중복된 데이터 가 저장된 배열을 인자로 넘기면 >>>> 값이 중복되면,
    count = Counter(a)  # 각 요소의 개수를 세기           # 3. 각 원소가 몇 번씩 나오는지 저장된 객체를 얻게 됩니다. >>>> 그게 몇 번 나왔는지 숫자로 값을 얻는다.
          
    return [key for key, value in count.items() if value == 1]  # 한 번만 등장하는 값만 필터링     

print(unique_elements(a)[0], unique_elements(b)[0])
                                                        # ex : Counter(["hi", "hey", "hi", "hi", "hello", "hey"])
                                                        #      Counter({'hi': 3, 'hey': 2, 'hello': 1})

                                                        #      Counter("hello world")
                                                        #      Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

                                                        #      counter = Counter("hello world")
                                                        #      counter["o"], counter["l"]
                                                        #      (2, 3)




