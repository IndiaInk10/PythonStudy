# 코딩, 영어 성적을 입력받고
# 성적에 따라서 각 과목의 평점에 구하고
# 최종 학점을 계산해서 출력하는 프로그램을 작성하세요
# 최종 학점은 소숫점 두번째 자리까지 출력하세요
#
# 평점산출방식
# 90점 이상 A
# 90점 미만 80점 이상 B
# 80점 미만 60점 이상 C
# 60점 미만 F
#
# 학점산출방식
# A = 4
# B = 3
# C = 2
# F = 0
# 으로 계산해서 전체 과목의 평균이 최종학점

coding = int(input())
English= int(input())

A = 4
B = 3
C = 2
F = 0

if coding >= 90 :
    coding = A
elif 80 <= coding < 90 :
    coding = B
elif 60 <= coding < 80 :
    coding = C
elif 60 > coding :
    coding = F

if English >= 90 :
    English = A
elif 80 <= English < 90 :
    English = B
elif 60 <= English < 80 :
    English = C
elif 60 > English :
    English = F
print(coding, English)

total = coding + English
average= total/2
grade = None

if average >= A :
    grade = 'A'
elif B <= average < A :
    grade = 'B'
elif C <= average < B :
    grade = 'C'
elif C > average :
    grade = 'F'

print('%.2f' %(average), ' ', grade)