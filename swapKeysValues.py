# 2. Write a program to swap keys and values in a dictionary.
d = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in d.items()}
print(swapped)
