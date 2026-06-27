#sum of digits
n=int(input("enter number:"))
s=0
while(n>0):
    d=n%10
    s=s+d
    n//=10
print("sumofdigit:",s)
#reverse a number
n=int(input("enter number:"))
s=0
while(n>0):
    d=n%10
    s=s*10+d
    n//=10
print("reverseofnumber:",s)
#count digits in a number
n=int(input("enter number:"))
if n==0:
    print(1)
else:
    count=0
    while(n>0):
        count+=1
        n//=10
    print("countofdigit:",count)
#check even or odd
n=int(input("enter number:"))
if n%2==0:
    print("even number")
else:
    print("odd number")
#prime number
n=int(input("enter number:"))
if n<=1:
    print("not prime")
else:
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            print("not prime")
            break
    else:
        print("prime")
#factorial number
n=int(input("enter number:"))
fact=1
for i in range(1,n+1):
    fact*=i 
print(fact)
#find factors of number
n=int(input("enter number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")
print()
#palindrome number
n=int(input("enter number:"))
temp=n
s=0
while(n>0):
    d=n%10
    s=s*10+d
    n//=10 
if s==temp:
    print("palindrome")
else:
    print("not palindrome")
#armstrong number
n=int(input("enter number:"))
temp=n
s=0
r=len(str(n))
while(n>0):
    d=n%10
    s=s+d**r
    n//=10 
if s==temp:
    print("armstrong")
else:
    print("not armstrong")
#gcd
a=int(input("enter number:"))
b=int(input("enter number:"))
while b!=0:
    a,b=b,a%b 
print("gcd=",a)


