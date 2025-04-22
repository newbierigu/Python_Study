# 사칙연산 계산기 만들기.

class FourCal:

    def __init__(self, first, second): # 생성자 init 사용(class를 호출하여 class내 객체(인스턴스) 사용 시 자동으로 init 먼저 사용됨)
        self.first = first
        self.second = second

    def setdata(self, first, second): # 값을 저장하는 메서드 만들기 # self는 함수 자기자신을 뜻함 (파이썬에서만 명시적으로 사용)
        self.first = first
        self.second = second

    def add(self): # 덧셈 메서드
        result = self.first + self.second
        return result
    
    def sub(self): # 뺄셈 메서드
        result = self.first - self.second
        return result
    
    def mul(self): # 곱셈 메서드
        result = self.first * self.second
        return result
    
    def div(self): # 나눗셈 메서드
        result = self.first / self.second
        return result
    

class MoreFourClass(FourCal): # 클래스 상속 개념(새로만든 class에 괄호붙이고 안에 상속할 class 명을 써줌)
    def pow(self):
        result = self.first ** self.second
        return result


class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
        
a = SafeFourCal(4, 0)

print(a.div())
