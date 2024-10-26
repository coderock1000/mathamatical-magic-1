def binary_to_int(binary_input):
    binary_dict = {'0': 0, '1': 1}
    result_int = 0
    length = len(binary_input)
    
    for i in range(length):
        result_int += binary_dict[binary_input[length - 1 - i]] * (2 ** i)

    return result_int

binary = input('Input binary number: ')
print('Decimal equivalent: ', binary_to_int(binary))
