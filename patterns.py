print("square pattern")
n=3
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
print("right pattern")
n=5
for i in range(n):
    for j in range(i+1):
            print("*",end=" ")
    print()
print("number triangle")
n=3
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print("repeated number triangle")
n=3
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
print("alphabet triangle")
n=3
val=65
for i in range(n):
    for j in range(i+1):
        print(chr(val+j),end=" ")
    print()
print("invert triangle")
n=5
for i in range(n-1,-1,-1):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("inverted number triangle")
n=5
for i in range(n-1,-1,-1):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
print("continous number pattern")
n=3
val=1
for i in range(n):
    for j in range(i+1):
        print(val,end=" ")
        val+=1
    print()
print("pyramid pattern")
n=5
for i in range(n):
    for j in range(n -i -1):
        print(" ",end=" ")
    for j in range(2 * i + 1):
        print("*",end=" ")
    print()
print("right angled star triangle")
n=5
for i in range(n):
    for j in range(n -i -1):
        print(" ",end=" ")
    for j in range(i + 1):
        print("*",end=" ")
    print()