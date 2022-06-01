# 파이참 파이썬 주석처리 단축키: ctrl + /


# 표현식을 통한 문자를 숫자로 치환해서 표기
# print("100") X
print("%d" % 100)  # 서식지정자를 통해 숫자 100을 출력
print("%d + %d = %d" % (10, 20, 10 + 20))  # 여러 서식지정자를 통해 한번에 출력 가능

# 서식지정자 종류
# %d: 10진수 / %x 16진수 / %o 8진수
# %f: 실수   / %c 문자   / %s 문자열
print("%d / %d  = %.1f" % (100, 200, 100/200))

# 구체적인 서식지정 방법들
# %5d 정수부 5자리를 잡고 출력 / %05d 정수부 5자리를 잡고 빈 부분은 0으로 채워서 출력
# %7.3f 총 7자리를 잡고 소수부는 그 상태에서 3자리를 잡고 빈 부분은 0으로 채워서 출력


# Escape char
# \n, \t, \\, \', \"

# Type 확인
a = 100
b = "100"
c = 100.0
print(type(a))
print(type(b))
print(type(c))


# Data type
# boolean(True, False), int, float, complex number(복소수: 2+3j), str
# list: 순서가 있는 값들의 집합
# tuple: 읽기전용 list
# set: 순서가 없고 중복되지 않는 값들의 집합
# dict: 키와 값이 쌍으로 데이터를 저장

# Typecasting
# data type()
num = int(input("값을 입력해주세요: "))

'''
여러줄 주석 처리하는 방법은 이런식으로 가능합니다.
'''