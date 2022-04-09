a = float(input('AMOUNT OF DOLLARS SUBMITTED:'))
print("YOUR CHANGE IS .....")
s = int(a / 20)
print(s, 'TWENTIES')
remainder1 = float(a % 20)
t = int(remainder1/10)
print(t, 'TENS')
remainder3 = float(remainder1 % 10)
u = int(remainder3 / 5)
print(u, 'FIVES')
remainder4 = float(remainder3 % 5)
v = int(remainder4 / 1 )
print(v, 'ONES')
remainder5 = float(remainder4 % 1)
w = int(remainder5 / 0.25)
print(w, 'QUARTERS')
remainder6 = float(remainder5 % 0.25)
x = int(remainder6 / 0.1)
print(x, 'DIMES')
remainder7 = float(remainder6 % 0.1)
y = int(remainder7 / 0.05)
print(y, 'NICKELS')
remainder8 = float(remainder7 % 0.05)
z = int(remainder8 / 0.01)
print(z, 'PENNIES')







