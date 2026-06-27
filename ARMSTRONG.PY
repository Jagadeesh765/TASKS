n=int(input("enter number:"))
t=n
s=len(str(n))
l=0
while(n>0):
    digit=n%10
    l+=digit ** s
    n//=10
if(t==l):
    print("Armstrong number:",t)
else:
    print("Not Armstrong:",t)