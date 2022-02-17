def computegrade():
    try:
        x = float(input("ENTER SCORE:"))
        if x > 1.0:
            print("ERROR, SCORE EXCEEDS RANGE")
        elif x < 0:
            print("ERROR, SCORE IS BELOW THE RANGE")
        else:
            if x >= 0.9:
                print("A")
            elif x >= 0.8:
                print("B")
            elif x >= 0.7:
                print("C")
            elif x >= 0.6:
                print("D")
            else:
                print("F")
    except:
        print("INVALID INPUT OF SCORE")


computegrade()

