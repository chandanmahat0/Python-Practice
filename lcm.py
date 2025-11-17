# 12. Find LCM of two numbers given by user.
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(abs(a*b) // math.gcd(a, b))
