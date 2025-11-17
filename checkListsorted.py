# 11. Check if user list is sorted.
lst = list(map(int, input("Enter list: ").split()))
print(all(lst[i] <= lst[i+1] for i in range(len(lst)-1)))
