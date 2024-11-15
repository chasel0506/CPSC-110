# read input
price = float(input('Please Enter the Price of Your Purchase: '))

# calculate GST PST Total
GST = price * 0.05
PST = price * 0.07
Total = price + GST + PST

# format all
formatted_price = format(price,'.2f')
formatted_GST = format(GST, '.2f')
formatted_PST = format(PST, '.2f')
formatted_Total = format(Total, '.2f')

# print the result
print('GST: $', formatted_GST)
print('PST: $', formatted_PST)
print('-------------------------------------------')
print('Total: $ ', formatted_Total)

# read input
cash = float(input('Enter Cash Paid: '))

# calculate the coins to be given
change = cash - Total
print(change,' is equal to:')

Tenner = change // 10
change = change % 10

Fin = change // 5
change = change % 5

Toonie = change // 2
change = change % 2

Loonie = change // 1
change = change % 1

Quarter = change // 0.25
change = change % 0.25

Dime = change // 0.1
change = change % 0.1

Nickel = change // 0.05
change = change % 0.05

Penny = change // 0.01
change = change % 0.01

# print the result
print(int(Tenner), 'Tenners')
print(int(Fin), 'Fins')
print(int(Toonie), 'Toonies')
print(int(Loonie), 'Loonies')
print(int(Quarter), 'Quarters')
print(int(Dime), 'Dimes')
print(int(Nickel), 'Nickels')
print(int(Penny), 'Pennies')