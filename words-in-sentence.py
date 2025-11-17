# 8. Count words longer than 5 characters in a sentence.
sentence = input("Enter a sentence: ")
count = sum(1 for w in sentence.split() if len(w) > 5)
print(count)
