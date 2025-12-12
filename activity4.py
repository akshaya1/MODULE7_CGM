# --------------------------------------------
# Python String Operations – Complete Program
# --------------------------------------------

# Creating strings
s1 = "Hello"
s2 = "Python"
s3 = "  Welcome to Python Programming  "

print("String 1:", s1)
print("String 2:", s2)
print("String 3:", s3)

print("\n------ Basic Operations ------")

# Concatenation
print("Concatenation:", s1 + " " + s2)

# Repetition
print("Repetition:", s1 * 3)

# Length
print("Length of s1:", len(s1))

print("\n------ Indexing and Slicing ------")

# Indexing
print("s1[0]:", s1[0])
print("s1[-1]:", s1[-1])  # Last character

# Slicing
print("s1[0:3]:", s1[0:3])
print("s2[1:5]:", s2[1:5])
print("s3 strip spaces:", s3.strip())

print("\n------ String Functions ------")

print("Uppercase:", s2.upper())
print("Lowercase:", s2.lower())
print("Title Case:", s2.title())
print("Swapcase:", s2.swapcase())
print("Starts with 'Py':", s2.startswith("Py"))
print("Ends with 'on':", s2.endswith("on"))
print("Count of 'o' in s2:", s2.count("o"))
print("Index of 'o' in s2:", s2.index("o"))
print("Replace 'Python' with 'Coding':", s2.replace("Python", "Coding"))

print("\n------ Splitting and Joining ------")

sentence = "apple,banana,orange"
print("Split sentence:", sentence.split(","))

words = ["I", "love", "Python"]
print("Join words:", " ".join(words))

print("\n------ Checking Types ------")

check = "Hello123"
print("Is Alpha:", check.isalpha())   # Only letters?
print("Is Digit:", check.isdigit())   # Only digits?
print("Is Alphanumeric:", check.isalnum())  # Letters + digits?
print("Is Lower:", check.islower())
print("Is Upper:", check.isupper())

print("\n------ String Formatting ------")

name = "Aman"
age = 12
print("Using format():", "My name is {} and I am {} years old".format(name, age))
print(f"Using f-string: My name is {name} and I am {age} years old")

print("\n------ Membership Operators ------")

print("'Py' in s2:", "Py" in s2)
print("'xyz' not in s2:", "xyz" not in s2)

print("\n------ Escape Characters ------")

print("New line:\nHello")
print("Tab:\tPython")
print("Single quote: \'Demo\'")
print("Double quote: \"Demo\"")

print("\n------ End of String Operations Program ------")
