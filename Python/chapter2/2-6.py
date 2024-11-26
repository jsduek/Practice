# 집합 자료형 : set

# s1 = set([1, 2, 3])
# # s1 = set([1, 2, 3]) // s1 = {1, 2, 3} 둘 다 같음
# # s1 = set("Hello") -> {'o', 'e', 'l', 'H'}  -> 집합은 순서 없이 랜덤으로 나타낸다.중복은 허용하지 않는다.
# # 집합 자료형은 index가 불가하기 때문에 아래 l1 과 같이 list로 데이터 변형을 해줘야 한다.// tuple도 가능
# l1 = list(s1)
# print(l1)

# 교집합, 합집합, 차집합
# 교집합 = s1 & s2 또는 .intersection 이라는 함수 사용 : s1.intersection(s2) 
# 합집합 = s1 | s2 또는 .union 이라는 함수 사용 : s1.union(s2)
# 차집합 = s1 - s2 기본적으로 - 사용 허자먼 (a - b) 의 성질로 a - b 와 b- a의 값이 다르다. 또는 .difference 라는 함수 사용 : s1.difference(s2) 마찬가지로 s1 과 s2의 위치가 바뀌면 값이 다르다.
# s1 = set([1, 2, 3, 4, 5, 6])
# s2 = set([4, 5, 6, 7, 8, 9])
# print(s1 - s2) = {1, 2, 3}
# print(s2 - s1) = {8, 9, 7}

# 집합 함수
# 값 1개 추가하기 = .add()
# 값 여러개 추가하기 = .update([])
# 특정 값 제거하기 = .remove()
s1 = set([1, 2, 3])
s1.add(4)
print(s1)