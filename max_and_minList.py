#Find max and min without using max() or min().

numbers = list(map(int, input("Enter numbers: ").split()))
max_val = min_val = numbers[0]

for n in numbers:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Max:", max_val)
print("Min:", min_val)
