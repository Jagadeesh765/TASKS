binary=input("enter binary number:")
decimal=int(binary,2)
print("Decimal =",decimal) 
#-----------------------------------#
binary=input("enter binary number:")
decimal=0
power=0
for digit in binary[::-1]:
    decimal+=int(digit) * (2 ** power)
    power+=1
print("Decimal =", decimal)



