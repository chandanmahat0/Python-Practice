# 6. Write a program to flatten a nested list.
nested = eval(input("Enter nested list: "))
flat = [x for sub in nested for x in sub]
print(flat)

