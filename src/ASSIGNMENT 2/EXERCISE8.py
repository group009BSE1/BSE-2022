c = float(input("INITIAL INVESTMENT:"))
r = 0.02
t = float(input("NUMBER OF YEARS TILL MATURATION:"))
n = float(input("NUMBER OF TIMES THE INTEREST IS COMPOUNDED PER YEAR:"))
p = c * (1 + r / n) ** (t * n)
x = round(p, 2)
print("FINAL VALUE OF THE INVESTMENT IS: ", x)

