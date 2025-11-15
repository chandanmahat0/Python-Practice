# Remove duplicates from a list while preserving order.

lst = list(map(int, input().split()))
unique = []

for x in lst:
    if x not in unique:
        unique.append(x)

print(unique)
