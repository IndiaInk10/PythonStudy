def get_average_score(name, **kwargs):
    cnt = 0
    average = 0

    cnt = len(kwargs)

    for value in kwargs.values():
        average += value

    average /= cnt
    return cnt, average

n, avg = get_average_score("홍길동", korean=95, math=100, english=90)
print(n, "과목의 평균 점수:", avg, "\n")

n, avg = get_average_score("홍길동", math=90, english=90, music=80, biology=90)
print(n, "과목의 평균 점수:", avg, "\n")