# ------------------ Arithmetic ------------------
a, b = 10, 3
print(a+b, a-b, a*b, a/b, a//b, a%b, a**b)

# ------------------ Assignment ------------------
a = 10
a += 5
a -= 2
a *= 2
a /= 2
a //= 2
a %= 3
a **= 2
print(a)

# ------------------ Comparison ------------------
a, b = 10, 20
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# ------------------ Logical ------------------
print(a>5 and b<30)
print(a>20 or b<30)
print(not(a==10))

# ------------------ Bitwise ------------------
a, b = 5, 3
print(a&b, a|b, a^b, ~a, a<<1, a>>1)

# ------------------ Membership ------------------
x = [1,2,3,4]
print(2 in x, 10 not in x)

# ------------------ Identity ------------------
a = [1,2]
b = a
c = [1,2]
print(a is b, a is c, a is not c)

# ------------------ Conditional ------------------
age = 18
print("Adult" if age>=18 else "Minor")

# ------------------ Lambda ------------------
square = lambda x: x*x
print(square(5))

# ------------------ List Comprehension ------------------
print([x*x for x in range(5)])

# ------------------ Dictionary Comprehension ------------------
print({x:x*x for x in range(5)})

# ------------------ Set Comprehension ------------------
print({x*x for x in range(5)})

# ------------------ Generator ------------------
g = (x*x for x in range(5))
print(list(g))

# ------------------ Built-in Functions ------------------
print(abs(-10))
print(round(5.678,2))
print(pow(2,5))
print(max(5,8,2))
print(min(5,8,2))
print(sum([1,2,3]))
print(len([1,2,3]))
print(divmod(10,3))

# ------------------ Type Conversion ------------------
print(int("10"))
print(float(10))
print(str(100))
print(bool(1))
print(list("ABC"))
print(tuple([1,2,3]))
print(set([1,2,2,3]))

# ------------------ String ------------------
s = "Python"
print(s.upper())
print(s.lower())
print(s.replace("P","J"))
print(s.split("t"))
print("-".join(["A","B","C"]))

# ------------------ List ------------------
l = [1,2,3]
l.append(4)
l.insert(1,10)
l.remove(2)
l.pop()
l.sort()
l.reverse()
print(l)

# ------------------ Tuple ------------------
t = (5,3,8)
print(len(t), max(t), min(t))

# ------------------ Set ------------------
A = {1,2,3}
B = {3,4,5}
print(A|B)
print(A&B)
print(A-B)
print(A^B)

# ------------------ Dictionary ------------------
d = {"a":1,"b":2}
print(d.keys())
print(d.values())
print(d.items())
print(d.get("a"))

# ------------------ Mathematical Formulas ------------------
r = 5
print("Area =", 3.14*r*r)
print("Circumference =", 2*3.14*r)

P, R, T = 1000, 5, 2
print("Simple Interest =", (P*R*T)/100)
print("Compound Interest =", P*(1+R/100)**T-P)

marks, total = 450, 500
print("Percentage =", (marks/total)*100)

a, b, c = 10, 20, 30
print("Average =", (a+b+c)/3)

n = 5
print("Square =", n**2)
print("Cube =", n**3)
print("Square Root =", n**0.5)

# ------------------ Swap ------------------
x, y = 10, 20
x, y = y, x
print(x, y)