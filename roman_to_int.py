def romantoint(romanInput):
    roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10,'V':5, 'I':1}
    result_int = 0
    for i in range(0, len(romanInput)-1):
        if roman[romanInput[i]] < roman[romanInput[i+1]]:
            result_int -= roman[romanInput[i]]
        else:
            result_int += roman[romanInput[i]]
    return result_int+roman[romanInput[-1]]

roman = input('Intput roman numeral: ')
print('Integer equivalent: ', romantoint(roman))
    