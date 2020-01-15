


def raise_to_power(base_num, pow_num):
#store the result, rn result=1
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))