# Count the frequency of each word in a given sentence.

from collections import Counter

sentence = input("Enter sentence: ").lower().split()
frequency = Counter(sentence)

for word, count in frequency.items():
    print(word, ":", count)
