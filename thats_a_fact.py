def print_factors(numbers):
    print('The fators of ',numbers, 'are: ')
    for i in range(1, numbers+1):
        if numbers % i == 0:
            print(i)

numbers = int(input('enter your number to get factors: '))

print_factors(numbers)