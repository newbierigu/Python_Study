# 딕셔너리는 key : value 로 이루어진 자료를 의미미함
# API에서 많이 활용됨.

# 딕셔너리 예제
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dic)


# value 값에 리스트도 들어감 (key에는 리스트가 안됨. key 값으로 value 값을 불러오기 때문에 immutable 자료형을 써야 함)
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}


# 딕셔너리 내 항목 추가하기 x[] = ''
a = {'인사' : 'hi'}
a['상태'] = '졸림'    # a 딕셔너리에[추가할 키값값] = '추가할 벨류값'
print(a)


# key 값으로 value 값 불러오기 dic['key']
dic = {'name' : 'pey', 'phone' : '010-9999-1234', 'birth' : '1129'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])


# key 값이 중복되면.....
dic = {'key1' : 'value1', 'key1' : 'value2', 'key1' : [1, 2, 3]}
print(dic)
# {'key1': [1, 2, 3]} 마지막 key1 값 만 출력되고 나머지 삭제됨


############################################################################
# 딕셔너리 관련 함수.



# key들만 모아서 보기 dic.keys()
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}
print(dic.keys())
# dict_keys(['key1', 'key2', 'key3'])


# value 들만 모아서 보기 dic.values()
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}
print(dic.values())
# dict_values(['value1', 'value2', [1, 2, 3]])


# key/value 쌍으로 얻기 dic.items()
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}
print(dic.items())
# dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', [1, 2, 3])])


# key/value 쌍으로 모두 지우기 dic.clear()
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}
dic.clear()
print(dic)
# {}


# get 함수 사용하여 value 값 얻기 dic.get()
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}
print(dic.get('name', '값이 없습니다.')) 
# dic.get('name') 만 적었다면 None으로 응답했을텐데, 뒤에 ('name', '값이 없습니다.') 라고 적어놓아서 해당 str을 리턴함
# print(dic['name'])  << get 함수와 차이점 : 없는 값이라고 KeyError 발생됨
print(dic.get('key3'))
# [1, 2, 3]


# 딕셔너리 내 해당 key가 존재하는지 - key in dic
dic = {'key1' : 'value1', 'key2' : 'value2', 'key3' : [1, 2, 3]}

print('key1' in dic)  # True
print('birth' in dic) # False
print('key3' in dic)  # True
print('name' in dic)  # False
