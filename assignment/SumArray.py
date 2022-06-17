import numpy as np
list1 = [[10, 10], [20, 30]]
print(np.mean(list1, axis=0))
aveList = [sum(list1[0]) / len(list1[0]), sum(list1[1]) / len(list1[1])]
print(aveList)