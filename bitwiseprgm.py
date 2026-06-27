# ------------------ Bitwise Operators ------------------

a = 5      # 0101
b = 5      # 0101
c = 3      # 0011
n = 1

print("a =", a)
print("b =", b)
print("c =", c)

# 1. XOR (^) - Same Values
print("\n1. XOR of Same Values")
print("5 ^ 5 =", a ^ b)      # Output: 0

# 2. XOR - Different Values
print("\n2. XOR of Different Values")
print("5 ^ 3 =", a ^ c)      # Output: 6

# 3. AND (&)
print("\n3. AND Operation")
print("5 & 3 =", a & c)      # Output: 1

# 4. OR (|)
print("\n4. OR Operation")
print("5 | 3 =", a | c)      # Output: 7

# 5. NOT (~)
print("\n5. NOT Operation")
print("~5 =", ~a)

# 6. Left Shift (<<)
print("\n6. Left Shift")
print("5 << 1 =", a << 1)

# 7. Right Shift (>>)
print("\n7. Right Shift")
print("5 >> 1 =", a >> 1)

# 8. Check Even or Odd using AND
print("\n8. Even or Odd")

if n & 1:
    print(n, "is Odd")
else:
    print(n, "is Even")

# Change n and test again
n = 8

if n & 1:
    print(n, "is Odd")
else:
    print(n, "is Even")