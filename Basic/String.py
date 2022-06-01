# Can store string in editor write form
editorString = """Hello World!
Bye World..."""
print(editorString)


# To lower / To Upper
print(editorString.upper())
print(editorString.lower())
# Check upper
print(editorString.isupper())
# Replace string, Must store
print(editorString.replace("World", "Food"))

# Find value of index, start from argument index
print(editorString.index("World", 12)) # Second World start index

# Find and Index(Occaure Error)
print(editorString.find("Food")) # return -1 if not found
# print(editorString.index("Food"))


# String format / Way 1: %d or else
# Way 2: "{}".format(value)
print("나는 {}살입니다.".format(2))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# Can set index of output format
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))
# Way 3: "{Variable}.format(Variable=value}"
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=3, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=3))
# Way 4: f""
age = 4
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


# Escape character
# \r: Move cursor to Start of string
print("Red Apple\rPine")

# \b: backspace
print("Redd\bApple")


# url = input("Site URL: ")
url = "https://youtube.net"
url = url[len("https://"):] # url.replace("https://", "")
url = url[:url.index('.')]
password = url[:3]
password += str(len(url)) + str(url.count('e')) + '!'
print(f"생성된 비밀번호 : {password}")