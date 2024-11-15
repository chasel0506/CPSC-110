# input the temp and unit
# c_unit = current unit, t_unit = target unit, temp = temperature
temp = float(input('Enter the temperature: '))
c_unit = input('Enter the current unit (C=Celsius, F=Fahrenheit or K=Kelvin): ')
t_unit = input('Enter the target unit (C=Celsius, F=Fahrenheit or K=Kelvin): ')

# calculate
if c_unit == 'C':
    if t_unit == 'F':
        temp = 9/5 * temp + 32
    elif t_unit == 'K':
        temp = temp + 273
        
if c_unit == 'F':
    if t_unit == 'C':
        temp = 5/9 * (temp - 32)
    elif t_unit == 'K':
        temp = 5/9 * (temp - 32) + 273
        
if c_unit == 'K':
    if t_unit == 'C':
        temp = temp - 273
    elif t_unit == 'F':
        temp = 9/5 * (temp - 273) + 32
    
print(f'Converted to the target unit temperature is: {temp} ◦{t_unit}')