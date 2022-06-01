# Key can be any data type(?)
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet.get(100))
# print(cabinet[5]) # None index access occaure KeyError
# if KeyError return other value use get
print(cabinet.get(5)) # it's like index and find method
print(cabinet.get(5, "사용 가능"))

# Check Key in Dictionary
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국"  # replace 유재석 as 김종국
cabinet["C-20"] = "조세호"
print(cabinet)

# Delete key and value in Dictionary
del cabinet["A-3"]

# Get Keys / Get Values / Get Pairs
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items()) # return Tuple

# Clear Dictionary
cabinet.clear()
print(cabinet)