# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))
# ['1', ' 2', ' 3', ' 4', ' 5', ' 6'] 지정한 문자 기준으로 요소를 나눈다.
# 하지만 리스트를 보면 공백이 있어서 거슬린다.
# 기준을 ". "로 바꿔보자.
print(my_string.split(". "))
# ['1', '2', '3', '4', '5', '6'] 공백이 삭제됐다.

full_name = "Kim, yuna"
print(full_name.split(",")) 
# ['Kim', ' yuna']로 출력된다. 마찬가지로 split 기준을 바꿔보자.
print(full_name.split(", ")) 
# ['Kim', 'yuna'] 정상 출력된다.

# 위 값들을 사용하려면,
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name ,last_name)
# 이렇게 사용할 수 있다.


# 이렇 상황을 가정해보자.
print("     \n\n  2    \t   3   \n   5 7 11     \n\n")
'''

  2        3
   5 7 11

'''
# 위와 같이 이상하게 출력된다.
# 숫자들을 제외하면 모두 화이트 스페이스이다.
# 만약 화이트 스페이스 기준으로 나누고 싶다면 .split을 하고 ()파라미터를 안넘겨주면 된다.
print("     \n\n  2    \t   3   \n   5 7 11     \n\n".split())
# ['2', '3', '5', '7', '11'] 깔끔하게 정상 출력 된다.


# 주의 사항
# 만들어진 리스트에서 요소를 사용하고 싶다 가정해보자.
numbers = "     \n\n  2    \t   3   \n   5 7 11     \n\n".split()
print(numbers[0] + numbers[1])
# 5가 아니라 '23'이 나온다.
# split을 활용해서 리스트를 만들면 리스트 내 요소 값은 전부 문자열이다.
# 따라서 해당 값을 정수로 받고싶다면 int로 변환해줘야한다.
print(int(numbers[0]) + int(numbers[1]))
# 5 정상 출력 된다.