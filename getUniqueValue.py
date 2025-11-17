# 7. Write a program to get unique values from list of dictionaries.
data = eval(input("Enter list of dicts: "))
unique = list({d[list(d.keys())[0]] for d in data})
print(unique)
