def get_avergae_score(name, **kwargs):
    cnt = 0
    average = 0

    ### Modify code here ###
    for value in kwargs.values():
        average += value
        cnt += 1

    average /= cnt
    ### End of your code ###

    return cnt, average

n, avg = get_avergae_score("홍길동", korean=95, math=100, english=90)
print(n, "과목의 평균 점수:", avg, "\n")

n, avg = get_avergae_score("홍길동", math=90, english=90, music=80, biology=90)
print(n, "과목의 평균 점수:", avg, "\n")