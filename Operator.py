# print(출력할 내용, [sep = 구분자], [end = 끝문자])
# sep default = " "(띄어쓰기 한칸)
# end default = Enter(한 줄 개행)

# divide
a = 5 / 3
print("실수", a, sep=" : ")
a = 5 // 3
print("몫", a, sep=" : ")
a = 5 % 3
print("나머지", a, sep=" : ")
a = divmod(5, 3)
print("목과 나머지", a, sep=" : ")

# pow
a = 5 ** 3
print("단일대입연산자 5의 3제곱", a, sep=" : ")

# 위에 서술한 연산자도 복합대입 연산자로 사용가능
a = 5
a **= 3
print("복합대입연산자 5의 3제곱", a, sep=" : ")

# logical operator

# 파이썬 내장함수
# abs: 절대값, max: 최대값, min: 최소값, pow: 제곱
# round: 반올림(5일 경우, 앞자리가 짝수일때만 올림)