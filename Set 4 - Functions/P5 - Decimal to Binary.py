print('Decimal to Binary')

def pow2(num):
    last_square = 0
    for x in range(num + 1):
        if 2 ** x > num:
            return last_square
        else:
            last_square = 2 ** x

def decToBin(num):
    highest_power_of_two = 0
    bin_string = ""
    highest_power_of_two = pow2(num)
    while num != 0:
        if num - highest_power_of_two >= 0:
            num -= highest_power_of_two
            highest_power_of_two = int(highest_power_of_two / 2)
            bin_string += "1"
        else:
            highest_power_of_two = int(highest_power_of_two / 2)
            bin_string += "0"
    while highest_power_of_two >= 1:
        bin_string += "0"
        highest_power_of_two = highest_power_of_two / 2
    return bin_string

for x in range(1,101):
    print(decToBin(x))
