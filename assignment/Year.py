# 생년월일(YYMMDD)을 여섯자리 형식으로 입력 받아서 YYYY/MM/DD 형식으로 출력하려고 한다.
# 년의 범위 : 1910이상 2010 미만
# 월의 범위 : 1~12
# 일의 범위 : 2월은 29일까지, 4, 6, 9, 11월은 30일까지, 그 외는 31일까지
# 이 때, 입력받은 생년월일의 형식이 올바르지 않으면 "Wrong"를 출력하시오.
# (단, 입력받은 형식이 6자리가 아닌 경우는 고려하지 않는다.)
#
# [입력예시1]
# 030511
#
# [출력예시1]
# 2003/5/11
#
# [입력예시2]
# 201515
#
# [출력예시2]
# Wrong

birth = int(input())

year = birth // 10000
if year <= 9:
    year += 2000
elif year >= 10:
    year += 1900

month = (birth // 100) % 100
day = birth % 100


if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day <= 31:
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        print(year,'/',month,'/',day, sep='')
    else:
        print('Wrong')
elif month == 2:
    if day <= 29:
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        print(year, '/', month, '/', day, sep='')
    else:
        print('Wrong')
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day <= 30:
        if month < 10:
            month = '0' + str(month)
        if day < 10:
            day = '0' + str(day)
        print(year, '/', month, '/', day, sep='')
    else:
        print('Wrong')
else:
    print('Wrong')