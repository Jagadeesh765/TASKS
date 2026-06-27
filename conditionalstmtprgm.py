num=int(input("enter a number:"))
if num>0:
    print(num,"positive number")
elif num<0:
    print(num,"negative number")
else:
    print(num,"Zero")
###########----------#####
s1=int(input("enter s1 marks:"))
s2=int(input("enter s2 marks:"))
s3=int(input("enter s3 marks:"))
s4=int(input("enter s4 marks:"))
s5=int(input("enter s5 marks:"))
s6=int(input("enter s6 marks:"))
if s1>=35 and s2>=35 and s3>=35 and s4>=35 and s5>=35 and s6>=35:
    print("pass")
else:
    print("fail")
###########----------##### 
ch=input("enter a character:")
if ch>='A' and ch<='Z':
    print(ch,":UPPERCASE")
else:
    print(ch,":LOWERCASE")
