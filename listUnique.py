# 14. Check if all elements in user list are unique.
lst = list(map(int, input("Enter list: ").split()))
print(len(lst) == len(set(lst)))