print('Multiplying')

def multiply(int1, int2):
    if int2 == 1:
        return int1
    return int1 + multiply(int1, int2 - 1)
    
print(multiply(23,432))