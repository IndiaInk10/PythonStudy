# Dictionary: list that has key and value as pair
# no need index, need key
phone_book = {"홀길동":"010-1234-5678",
        "강감찬":"010-9876-5432",
        "이순신":"010-1234-0000",}

# use Dictionary with List like structure
info = []
for i in phone_book.keys():
    info.append({i: phone_book[i]})
print(info)

student_list = []
student_list.append({"학번":1000, "이름":"홍길동", "학과":"열공학과"})
student_list.append({"학번":1001, "이름":"강감찬", "학과":"체육학과"})
student_list.append({"학번":1002, "이름":"이순신", "학과":"물리학과"})
student_list.append({"학번":1003, "이름":"신사임당", "학과":"열공학과"})
for i in student_list:
    print("학번: %d, 이름: %s" % (i["학번"], i["이름"]))
    
print("==열공학과 학생 이름 출력==")
for i in student_list:
    if i["학과"] == "열공학과":
        print(i["이름"])