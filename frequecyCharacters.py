# 3. Write a program to find the frequency of each character in a string.
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
