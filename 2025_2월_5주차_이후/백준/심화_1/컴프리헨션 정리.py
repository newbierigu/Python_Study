# 0 ~ 10 에서 짝수만
list = range(0, 11)
list = [x for x in list if x % 2 == 0]
# 첫 번째 x는 x를 list에 넣어라 라는 뜻
# x.replace() or x + y 사용해도 된다.

# 두 번째 x는 list에서 뽑아온 요소를 저장하는 변수이다.


# in list 는 list의 요소 당 한 번씩 반복한다는 뜻이다.

# 세 번째 x는 두 번째 x를 if문에 넣은 것이다.
# 조건이 True라면 list에 첫 번째 x의 형태로 저장된다. 
# 첫 번째 x가 int이고 x - 1 이면 if 조건문 통과한 요소가 2일 때 list에 담기는 것은 1 이다.