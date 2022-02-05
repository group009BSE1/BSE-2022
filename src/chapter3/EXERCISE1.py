a = int(input('ENTER HOURS:'))
b = int(input('ENTER RATE:'))
if a > 40:
    c = (a - 40) * (15 / 10 * b)
    d = c + (40 * b)
    print('PAY:', d)
else:
    print('PAY:', a * b)


