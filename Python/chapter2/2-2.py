# # # # name = '홍길동'
# # # # age = 30
# # # # a= f'나의 이름은 {name}입니다. 나이는 {age * 2}입니다.'
# # # # print(a)

# # # ## 문자열 자료형 함수

# # # # a = "hobby"
# # # # print(a.count('b'))  ## -> a 에서 b의 갯수를 세줌
# # # # print(a.find('b')) ## a 에서 b 의 인덱스를 찾아줌 // 없는 것을 찾아라고 명령하면 -1 반환
# # # # print(a.index('b')) ## 없으면 오류로 반환

# # # a = ",".join('abcd')   # abcd 사이에 ,를 넣어줌 to do 같은 문자도 가능 // 리스트에도 사용 가능하다.
# # # print(a)

# # a = "HI"
# # # print(a.upper())  # 소문자에서 대문자로
# # print(a.lower())    # 대문자에서 소문자로

# a = " hi "
# print(a.strip())  # 양쪽 공백제거 (rstrip(오른쪽), lstrip(왼쪽))

# a = "Life is too short"
# print(a.replace("Life", "Your leg"))  # 앞의 문자열을 뒤의 문자열로 바꿔줌

a = "Life is too short"
print(a.split()) # 공백을 기준으로 나눠준다

