try:
    x = int(input('ENTER YOUR AGE:'))
    if x >= 18:
        print('YOU CAN VOTE')
    elif 0 < x <= 17:
        print('TOO YOUNG TOO VOTE')
    elif x < 0:
        print('YOU ARE A TIME TRAVELLER')
except:
    print('ERROR,PLEASE ENTER A NUMBER')
