#Check if the input is a palindrome.

def is_palindrome(x):
    x = str(x)
    return x == x[::-1]

item = input("Enter string/number: ")
print("Palindrome" if is_palindrome(item) else "Not Palindrome")
