# Q1 : 조건문의 참과 거짓
# 다음 코드의 결과값은?
a = "Life is too shortm you need python"

if "wife" in a: print ('wife')
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print ('shirt')
elif "need" in a: print('need')
else: print("none")

# 정답 : shirt


# Q2 : 3의 배수 구하기
# while 문을 사용해 1 부터 1000 까지의 자연수 중 3의 배수의 합을 구해보자.

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)





# Q3 : 별 표시하기
# while 문을 사용하여 (*)별을 표시하는 프로그램을 작성해보자
# 실행 결과
'''
*
**
***
****
*****
'''
# 정답
i = 0
while i < 5:
    i += 1
    print('*' * i)






# Q4 : 1 부터 100 까지 출력하기
# for 문을 사용하여 1 부터 100까지 출력하는 코드 생성

for i in range(1, 101):
    print(i)







# Q5 : 평균 점수 구하기
# 예시 : [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# 위 점수의 평균을 구하는 함수 생성

a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0

for score in a:
    total = score + total    # total += score
    average = total / len(a)
print(average)




# Q6 : 리스트 컴프리헨션 사용하기
# 다음 소스 코드를 컴프리헨션을 사용하여 표현하자
'''
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n * 2)
print(result)
'''

# 정답
numbers = [1, 2, 3, 4, 5]
result = [n * 2 for n in numbers if n % 2 == 1]
print (result)





