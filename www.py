# --- Variable declaration and types ---
a = 15
b = 12
print("Type of a:", type(a))   # Output: Type of a: <class 'int'>
print("Type of b:", type(b))   # Output: Type of b: <class 'int'>

# --- Basic arithmetic ---
print("a + b =", a + b)        # Output: a + b = 27
print("a - b =", a - b)        # Output: a - b = 3
print("a * b =", a * b)        # Output: a * b = 180
print("a / b =", a / b)        # Output: a / b = 1.25

# --- Type casting ---
c = int(a / b)                 # 1.25 is converted to an integer, so c = 1
print("c =", c, "| type:", type(c))   # Output: c = 1 | type: <class 'int'>

c = float(c)                   # Convert c to a float
print("c =", c, "| type:", type(c))   # Output: c = 1.0 | type: <class 'float'>

# --- Strings ---
message = "The result of a divided by b is?"
print(message + " " + str(c))  # Output: The result of a divided by b is? 1.0

# --- Comparison operators ---
print("a > b:", a > b)         # Output: a > b: True
print("a == b:", a == b)       # Output: a == b: False
