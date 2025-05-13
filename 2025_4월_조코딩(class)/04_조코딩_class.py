# 클래스 변수
# 클래스 내 공용으로 사용되는 변수 값을 뜻함
# a 처럼 변경할 수도 있음음

class Family:
    lastname = "김"


a = Family()
b = Family()
c = Family()

a.lastname = "박"

print(a.lastname)
print(b.lastname)
print(c.lastname)