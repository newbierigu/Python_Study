class Calculator:
    
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# class 를 사용해서 계산기 2개 역할을 만들었다.

# 뺄셈도 추가해보자.

'''
class Calculator:
    def __init__(self):
        self.result = 0
        
    def add(self, num):
        self.resulf += num
        return self.result
        
    def sub(self, num):
        self.result -= num
        return self.result
'''

# 위 함수 sub 처럼 class 에 뺄셈 함수 추가만 해도 사용할 수 있다다. 