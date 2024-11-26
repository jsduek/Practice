# 딕셔너리 {key : value}  -> api에 자주 활용됨
# 중괄호 {} 사용
# value 에 list 입력 가능
# dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

# 새로운 값 추가 (문자, 리스트 등 가능하다.)
# a = {1: 'a'}
# a[2] = 'b'
# print(a)

# 삭제(key를 지정해주면 그 해당 키밸류가 모두 삭제)
# a = {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
# del a['name'], [2] ## 콤마를 사용하여 한번에 여러개 삭제 가능
# print(a)

# 밸류를 가져오고 싶을 때
# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])


# 딕셔너리를 만들 때 
# key 는 무조건 하나여야 한다.(중복불가)
# key 는 변형되면 안된다.

# 관련 함수
# a = {}
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# a.keys() -> key 값만 가져온다 / 반대로  a.values() 눈 value 값만 가져온다
# list(a.keys) -> key 값을 간략한? list로 변환
# a.items() -> (key, value) 형식으로 쌍별로 나타내준다.
# a.clear() -> 딕셔너리 값을 모두 날린다.
# print(a['hi']) -> 없는 값이라 에러 / # print(a.get('hi')) -> None
# print(a.get('hi',"값이 없습니다.")) -> 값이 없는 경우 ,뒤의 문자 리턴/ 값이 있는 경우에는 딕트안의 value 리턴
# print('name' in a) -> 존재여부 확인(True or False)