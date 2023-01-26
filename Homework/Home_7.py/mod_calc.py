def sum_data(num_1, num_2):
    return num_1 + num_2

def sub_data(num_1, num_2):
    return num_1 - num_2

def mul_data(num_1, num_2):
    return num_1 * num_2

def div_data(num_1, num_2, par="/"):
    if par == "%":
        return round(num_1 % num_2, 2) 
    elif par == "//":
        return num_1 // num_2
    return num_1 / num_2


def pow_data(num_1, num_2):
    return num_1 ** num_2 

def sqrt_data(num_1):
    return num_1 ** 0.5                