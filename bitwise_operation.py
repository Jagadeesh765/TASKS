# Bitwise Operators Program

a = 5
b = 5

print("Value of a =", a)
print("Value of b =", b)

# 1. XOR of same values
print("\n1. XOR Operation")
print("a ^ b =", a ^ b)
print("Output: 0 (because both values are the same)")

# 2. AND Operation
print("\n2. AND Operation")
print("a & b =", a & b)

# 3. OR Operation
print("\n3. OR Operation")
print("a | b =", a | b)

# 4. NOT Operation
print("\n4. NOT Operation")
print("~a =", ~a)

# 5. Left Shift
print("\n5. Left Shift")
print("a << 1 =", a << 1)

# 6. Right Shift
print("\n6. Right Shift")
print("a >> 1 =", a >> 1)

# 7. Check whether 1 is Even or Odd using AND
print("\n7. Even/Odd Check Using AND")

n = 1

if (n & 1) == 1:
    print("1 is Odd")
else:
    print("1 is Even")

# 8. Practice all bitwise operators with another value
x = 5
y = 3

print("\n8. Practice All Bitwise Operators")
print("x =", x)
print("y =", y)

print("x & y =", x & y)
print("x | y =", x | y)
print("x ^ y =", x ^ y)
print("~x =", ~x)
print("x << 1 =", x << 1)
print("x >> 1 =", x >> 1)