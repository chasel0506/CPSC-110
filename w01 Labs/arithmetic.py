number = int(input('Enter a positive number: '))
a = number % 10
b = number // 10 % 10
c = number // 100 % 10
d = number // 1000

sum = a + b + c + d
product = a * b * c * d
backwards = a *1000 + b *100 + c *10 + d
doubled = number * 2
square_root = number ** 0.5

print(f'The sum of all the digits of the number: {sum}')
print('The product of all the digits of the number: ', product)
print('The number backwards: ',backwards)
print('The number doubled: ',doubled)
print('The square root of the number: ', square_root)