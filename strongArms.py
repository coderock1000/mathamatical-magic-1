num = int(input('enter your number: '))

digit = len(str(num))

resnumber = 0

temp = num
while temp > 0:
    dig = temp % 10
    resnumber += dig ** digit
    temp //= 10

if num == resnumber:
    print(num, 'is an Armstrong number')
else:
    print(num, 'Its not an armstrong number')
