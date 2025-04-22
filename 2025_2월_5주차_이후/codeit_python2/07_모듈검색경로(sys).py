# 파이썬 모듈 검색 경로
# sys라는 스탠다드 모듈을 사용함

import sys

print(sys.path) # path는 파이썬이 모듈을 찾기 위해 검색해보는 경로들이 저장되어 있음.
# ['c:\\Users\\nuwba\\Desktop\\Python_Study\\2025_2월_5주차_이후\\codeit_python2', 'c:\\Users\\nuwba\\AppData\\Local\\Programs\\Python\\Python313\\python313.zip', 'c:\\Users\\nuwba\\AppData\\Local\\Programs\\Python\\Python313\\DLLs', 'c:\\Users\\nuwba\\AppData\\Local\\Programs\\Python\\Python313\\Lib', 'c:\\Users\\nuwba\\AppData\\Local\\Programs\\Python\\Python313', 'c:\\Users\\nuwba\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages']
# 파이썬은 모듈을 찾기 위해 이 경로들을 순서대로 확인한다.
# 그리고 모듈을 못 찾으면 오류를 발생시킨다.



# sys.path에 경로를 새로 추가하는 방법.

# 1. sys.path에 .append()로 경로 추가하기.
# sys.path에 새로운 경로를 직접 추가하는 것이다.
# 위에서 출력해보았듯이 결국 list 형태이기 때문에 .append()로 추가가 가능하다.

# 예를 들어 sys.path에 바탕 화면의 경로를 추가하고 싶다면 아래와 같은 코드를 추가해 주면 된다.
'''
import sys
sys.path.append('/Users/codeit/Desktop') # macOS
sys.path.append('C:\\Users\\codeit\\Desktop') # Windows'
'''
# 윈도우의 경로 같은 경우 역슬래시를 2개 써 준다. '
# '프로그래밍에서는 \<char> 패턴을 가진 특수 문자들이 있다. '
# '예를 들어 \t는 탭을 뜻하고 \n은 새로운 줄을 뜻한다. '
# '윈도우 파일 경로는 \가 들어가기 때문에 \와 다음 문자가 특수 문자로 인식될 수도 있다 '
# '그래서 윈도우 파일 경로를 다룰 때는 \를 뜻하는 특수 문자, \\를 사용해야 한다.

# 저렇게 .append()를 시키면, sys.path가 검색할 때 바탕화면 경로도 찾아볼 수 있다.

# 바탕화면에 만들어논 test라는 모듈을 놓고 import를 시키면 이제 편안하게 사용 가능하다.
'''
improt sys
sys.path.append('C:\\Users\\codeit\\Desktop')

import test
'''
# 위 처럼 사용 가능하다.

# .append() 해주면 경로를 추가해줄 수 있지만, 프로그램이 종료되면 그 경로는 sys.path에서 사라진다.
# 그 경로에 있는 모듈을 쓰고 싶으면 매번 .append()를 사용해야 한다.

# 영구적으로 경로를 추가하는 방법은 나중에 배워보자.
