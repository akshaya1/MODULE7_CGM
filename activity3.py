# --------------------------------------------
# Python Operators – Complete Demonstration
# --------------------------------------------

print("------ Arithmetic Operators ------")
a = 10
b = 3

print("a + b =", a + b)     # Addition
print("a - b =", a - b)     # Subtraction
print("a * b =", a * b)     # Multiplication
print("a / b =", a / b)     # Division
print("a % b =", a % b)     # Modulus
print("a ** b =", a ** b)   # Exponent
print("a // b =", a // b)   # Floor division

print("\n------ Assignment Operators ------")
x = 5
print("x =", x)

x += 3   # x = x + 3
print("x += 3:", x)

x -= 2   # x = x - 2
print("x -= 2:", x)

x *= 4   # x = x * 4
print("x *= 4:", x)

x /= 3   # x = x / 3
print("x /= 3:", x)

x %= 2   # x = x % 2
print("x %= 2:", x)

x = 5
x **= 2  # x = x ** 2
print("x **= 2:", x)

x //= 2  # x = x // 2
print("x //= 2:", x)

print("\n------ Comparison Operators ------")
p = 10
q = 20

print("p == q:", p == q)
print("p != q:", p != q)
print("p > q:", p > q)
print("p < q:", p < q)
print("p >= q:", p >= q)
print("p <= q:", p <= q)

print("\n------ Logical Operators ------")
m = True
n = False

print("m and n:", m and n)
print("m or n:", m or n)
print("not m:", not m)

print("\n------ Identity Operators ------")
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is y:", x is y)       # False (different objects)
print("x is z:", x is z)       # True (same object)
print("x is not y:", x is not y)

print("\n------ Membership Operators ------")
fruits = ["apple", "banana", "cherry"]

print("'apple' in fruits:", "apple" in fruits)
print("'mango' not in fruits:", "mango" not in fruits)

print("\n------ Bitwise Operators ------")
a = 5   # 0101
b = 3   # 0011

print("a & b =", a & b)     # AND
print("a | b =", a | b)     # OR
print("a ^ b =", a ^ b)     # XOR
print("~a =", ~a)           # NOT
print("a << 1 =", a << 1)   # Left shift
print("a >> 1 =", a >> 1)   # Right shift

print("\n------ End of Operators Program ------")
