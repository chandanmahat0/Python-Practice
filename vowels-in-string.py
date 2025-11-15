#Write a program to count number of vowels in a string.

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

s = input("Enter text: ")
print("Vowel Count:", count_vowels(s))
