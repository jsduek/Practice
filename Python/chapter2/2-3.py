# 리스트 자료형
# -> 대괄호 사이에 콤마로 구분하여 입력/문자 숫자 등 다 담을 수 있다./리스트 안에 리스트를 또 넣어 줄 수 있다.
# 인덱싱 할 수 있다.
# 리스트안의 리스트는 그 자체로 인덱스 1 이다.  
# a = [1, 3, 5, 7, 9, ['a', 'b', 'v']] 
# print(a[-1][1])  

# 슬라이싱도 가능하다
# a = [1, 3, 5, 7, 9] 
# print(a[0::2])  

# 사칙연산 가능
# a = [1, 2, 3]
# b = [4, 5, 6]
# print(a + b)

# list 길이 구하기    /  string 문자열 (문자 + 리스트(배열))
# 형태가 다르면 안된다.
# a = [1, 2, 3]   
# print(a[2] * 3)  # operand = ()안의 양쪽을 말한다 

# 리스트 수정/ 삭제
# a = [1, 2, 3]
# a[2] = 4  수정
# del a[1]  삭제  -> 슬라이싱으로도 가능 del a[:1] 등등
# print(a)

# 리스트에 요소 추가
# a = [1, 2, 3]
# a.append(4)
# print(a)

# 리스트 정렬 / 알파벳도 가능
# a = [1, 2, 4, 3]
# a.sort()  -> 오름차순
# print(a)
# a.reverse() -> 내림차순
# print(a)
# print(a.index(3))

# 리스트 insert(삽입) remove(제거)
# a = [1, 2, 3, 1, 2, 3]
# # a.insert(1, 4) -> (위치, 삽입값)
# # a.remove(3)    -> 먼저 나오는 값 삭제
# print(a)

# 요소 끄집어 내기
# a = [1, 2, 3]
# print(a.pop()) -> 맨 마지막 요소를 리턴하고 삭제 // ()안에 위치 설정 가능
# print(a)

# print(a.count(1))  -> 괄호 안의 1의 개수를 리턴해준다.
# extend([4,5])  -> append 는 대괄호까지 들어가지만 extend는 괄호 안의 값만 추가가 된다.