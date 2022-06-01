# 데이터 관리는 List, Tuple, Set 또는 Dictionary를 통해 손쉽게 해줄 수 있다

scores = [85,70,90,98,87,68,77,100,75,80]
# total을 통해 list의 모든 값들의 합을 구할 수 있다
ave = sum(scores) / len(scores)
print("평균: %.2f" % ave)

ave = 0
count = 0
for i in scores:
    ave += i
    count += 1
ave /= count
print("평균: %.2f" % ave)


# List Method
# append: add value into end of list
numbers = []
for i in range(1, 11, 1):
    if str(i).count("3") > 0 or str(i).count("6") > 0 or str(i).count("9") > 0:
        numbers.append("*")
    else:
        numbers.append(i)
print("369가 들어간 수는 별로\n", numbers, sep="")
# insert: add value into index of list
numbers.insert(2, 5)
print("2번째에 5 추가", numbers, sep="\n")

# pop: return last inserted value and delete from list
print("마지막 %d이 빠진" % numbers.pop(), numbers)
# sort: sort list
sortList = [5, 2, 3, 1, 4]
sortList.sort()
print(sortList)

# reverse: reverse list
sortList.reverse()
print(sortList)

# index: find index of value
print("2의 인덱스는? %d" % sortList.index(2))

# remove: delete specificed value from list
sortList.remove(2)
print("2를 지운 list", sortList)

# extend: list + list
addList = range(10)
sortList += addList
print(sortList)
for i in range(len(addList)):
    sortList.pop()
sortList.extend(addList)
print(sortList)

# count: find value and count how many it is
print("List에서 1의 개수는? %d" % sortList.count(1))

# del: delete value of index from list
print(sortList, "에서 2번째 값 삭제", sep="\n")
del(sortList[2]) # or del sortList[2]
print(sortList)

# len: length of list
print("List의 길이는?", len(sortList))

# List Slicing [start:end(exclusive)
slicingList = sortList[0:3] # same as sortList[:3]
print("Slicing from 0 to 3(exclusive):", slicingList)
slicingList = sortList[3:]
print("Slicing from 3 to end:", slicingList)
slicingList = sortList[:]
print("Slicing from start to end(same as slicingList):", slicingList)
# skip index mean start or end index


# Tuple(Const List: Read Only!)
# Declare(Only Once!)
tNumbers = (0, 1, 2, 3, 4, 5)
print(tNumbers)
# Can do del when delete all of value from tuple
del(tNumbers)
print(tNumbers)

