# for(number of loops) range
# 0 to exclusive argument
for i in range(5):
    print("%d번째 반복중" % i)

# other way for set number of loops
# range(start=시작값, stop=종료값, step=한번에 증가되는 값)
for i in range(1, 10, 2):
    print("홀수 : %d" % i)

# for과 list의 연계 응용
print("[list 홀수]")
a = [1, 3, 5, 7, 9]
for i in a:
    print("홀수 : %d" % i)
a = "hello"
for i in a:
    print(i, end="")
print()
a = "This is impossible!"
count = 0
for i in a:
    if i == "i":
        count += 1
print("i의 개수 : %d" % count)