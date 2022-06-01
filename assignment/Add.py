def add_from_x1_to_x2(x1, x2):
    ret = 0
    ### Modify code here ###
    for i in range(x1, x2 + 1):
        ret += i
    ### End of your code ###
    return ret

ret = add_from_x1_to_x2(3,5)
print("ret: ", ret)
ret = add_from_x1_to_x2(-3,4)
print("ret: ", ret)