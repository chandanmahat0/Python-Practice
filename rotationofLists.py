# 15. Rotate a list by K steps.
lst = list(map(int, input("Enter list: ").split()))
k = int(input("Enter rotation steps: "))
rotated = lst[-k:] + lst[:-k]
print(rotated)
