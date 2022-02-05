try:
    x = int(input('ENTER NUMBER OF GUESTS:'))
    if x <= 50:
        print('THE TOTAL COST IS $4000 DOLLARS')
    elif x <= 100:
        print('THE TOTAL COST IS $10000 DOLLARS')
    elif x <= 200:
        print('THE TOTAL COST IS $15000 DOLLARS')
    else:
        print('THE TOTAL COST IS $20000 DOLLARS')
except:
    print('WRONG INPUT ENTERED')



