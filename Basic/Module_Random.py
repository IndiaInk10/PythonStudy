import random
# Generate 0.0 ~ 1.0 random value
print(random.random())
# Generate 0.0 ~ 10.0 random value
print(random.random() * 10)
# Generate from 1 to 46(exclusive) random value
print(random.randrange(1, 46))
# Generate from 1 to 46(inclusive) random value
print(random.randint(1, 46))


def SetOfflineMeeting():
    day = random.randint(4, 28)
    print("오프라인 스터디 모임 날짜는 매월 %d 일로 선정되었습니다." % day)


SetOfflineMeeting()