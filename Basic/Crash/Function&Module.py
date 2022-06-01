# 섭씨 to 화씨
def CtoF(_c):
    return _c * 1.8 + 32


c = 18
print(CtoF(c))


def CheckSecurity(password):
    nums = "0123456789"
    symbols = "!@#$%^&*()"
    difficulty = 0

    for i in password:
        if nums.count(i) > 0:
            difficulty += 1
        if symbols.count(i) > 0:
            difficulty += 1

    if difficulty >= 2:
        return "강함"
    elif difficulty == 1:
        return "보통"
    else:
        return "약함"


print(CheckSecurity("abc"))
print(CheckSecurity("abc1"))
print(CheckSecurity("abc1!"))


def PrimeNumber(num):
    isPrime = True
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        return "소수"
    else:
        return "소수 아님"


print(PrimeNumber(3))
print(PrimeNumber(10))


# Local Variable / Global Variable
def CalculateArea(radius):
    global gArea
    gArea = 3.14 * radius ** 2


gArea = 0
r = 5
CalculateArea(r)
print(gArea)

# Module like Static Class and Method
import MyModule
MyModule.HelloWorld()
MyModule.ByeWorld()

# Can skip Module name
from MyModule import *
HelloWorld()
ByeWorld()

# Make it independently