# 10. Remove punctuation from a string.
import string
s = input("Enter a string: ")
clean = "".join(ch for ch in s if ch not in string.punctuation)
print(clean)
