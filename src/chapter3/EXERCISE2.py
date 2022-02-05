a = input('ENTER HOURS:')
try:
    x = int(a)
    b = int(input('ENTER RATE:'))
    if x > 40:
        c = (x - 40) * (15 / 10 * b)
        d = c + (40 * b)
        print('PAY:', d)
    else:
        print('PAY:', a * b)
except:
    print('PLEASE INPUT A NUMERIC FIGURE')

