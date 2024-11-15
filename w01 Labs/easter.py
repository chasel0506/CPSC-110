year = int(input('Enter the year: '))

a = year // 100
b = year % 100
c = b // 4
d = b % 4
e = year % 19
f = a % 4
g = a // 4
h = (a + 8)// 25
i = (a - h +1)// 3
j = (19 * e + a - g - i + 15) % 30
k = (32 + 2 * f + 2 * c - j - d) % 7
l = (e + 11 * j + 22 * k) // 451
month = (j + k - 7 * l + 114)// 31
day = 1 + (j + k - 7 * l + 114) % 31
    
print('The date of Easter: ', day,month,year)