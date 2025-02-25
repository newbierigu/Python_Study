# 집합
# set() 으로 만듦
# 
s1 = set([1, 2, 3])      # set() 는 리스트/스트링 다 들어감
print(s1)
print(type(s1))
# {1, 2, 3}



s2 = set("hello")
print(s2)
# {'l', 'e', 'o', 'h'} 
# 집합의 특성 1 : 집합은 중복을 허가하지 않는다. 특징 2 : 집합은 순서가 따로 없다.
# 위 처럼 순서가 따로 없는 특징 때문에 인덱싱이 먹히질 않는다.



# 값을 가져오고 싶을 때 (인덱싱)
l1 = list(s1)       # list로 변환
print(l1)
# [1, 2, 3]
print(l1[0])
# 1

t1 = tuple(s1)      # tuple로 변환
print(t1)
# (1 ,2, 3)
print(t1[1])
# 2



# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))
# {4, 5, 6}



# 합집합
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))
# {1, 2, 3, 4, 5, 6, 7, 8, 9}



# 차집합
print(s1 - s2)                # {1, 2, 3}
print(s2 - s1)                # {8, 9, 7}
print(s1.difference(s2))      # {1, 2, 3}
print(s2.difference(s1))      # {8, 9, 7}


# 집합 자료형 관련 함수

# add
# 집합 내 1개의 값만 추가할 때 사용함 집합.add(넣을 값) list에선 append 와 비슷함
s1 = set([1, 2, 3])
s1.add(4)
print(s1)
# {1, 2, 3, 4}

# update
# 여러 개의 값(list)들을 추가할 때 사용함 집합.update([넣을 값]) list 에선 extend 와 비슷함
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
# {1, 2, 3, 4, 5, 6}

# remove
# 집합 내 특정 값을 지울 때 사용함 집합.remove(지울 값)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
# {1, 3}


# 언제 자주 활용하냐~
l1 = [1, 2, 2, 3, 3, 3, 3, 4]
s1 = list(set(l1))      # 리스트로 계속 활용하고 싶은데 고유한 값 하나씩만 남기고 싶을 때 많이 사용함
print(s1)
# [1, 2, 3, 4]