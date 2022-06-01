from math import pow

def calc_base_a_exponent_n(a, n):
    ### Modify code here ###
    for i in range(0, n + 1):
        print(a, "^", i, "=", pow(a,i))
    ### End of your code ###

calc_base_a_exponent_n(2, 3)
calc_base_a_exponent_n(3, 5)
calc_base_a_exponent_n(-2, 1)
calc_base_a_exponent_n(5, 0)