new = []
while True:
    num = input('Enter number: ')
    try:
        if num.lower() == 'done':
            print(f"maximum is", max(new))
            print(f"minimum is", min(new))
            break
        num = float(num)
    except:
        print('Invalid input')
        continue
    num = float(num)
    new.append(num)

