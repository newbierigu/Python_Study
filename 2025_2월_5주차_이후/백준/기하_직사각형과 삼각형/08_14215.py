# 문제
# 영선이는 길이가 a, b, c인 세 막대를 가지고 있고, 각 막대의 길이를 마음대로 줄일 수 있다.

# 영선이는 세 막대를 이용해서 아래 조건을 만족하는 삼각형을 만들려고 한다.

# 각 막대의 길이는 양의 정수이다
# 세 막대를 이용해서 넓이가 양수인 삼각형을 만들 수 있어야 한다.
# 삼각형의 둘레를 최대로 해야 한다.
# a, b, c가 주어졌을 때, 만들 수 있는 가장 큰 둘레를 구하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 a, b, c (1 ≤ a, b, c ≤ 100)가 주어진다.

# 출력
# 첫째 줄에 만들 수 있는 가장 큰 삼각형의 둘레를 출력한다.



Triangle = list(map(int,input().split()))

Triangle.sort()

if Triangle[0] + Triangle[1] > Triangle[2]:
    print(sum(Triangle))
    
else:
    x = Triangle[2] = (Triangle[0] + Triangle[1] - 1)
    print(sum(Triangle))





'''풀이 과정

a b c 중 제일 큰 숫자 제외 나머지를 더해주고, 
더한 값보다 1 작은 숫자로 줄여서 둘래 길이 구하면 만들 수 있는 최대 둘랫 값임.

c가 가장 큰 값이면
a + b = x

c = x - 1

print(x + c)'''