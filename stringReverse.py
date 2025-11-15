#Reverse a string without using built-in reverse function.

s = input("Enter string: ")

# Method 1: Slicing
print("Reverse:", s[::-1])

# Method 2: Loop
rev = ""
for char in s:
    rev = char + rev
print("Reverse:", rev)

# Method 3: Using reversed()
print("Reverse:", "".join(reversed(s)))
