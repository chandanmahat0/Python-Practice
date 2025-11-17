# 17. Filter even numbers using lambda.
lst = list(map(int, input("Enter list: ").split()))
evens = list(filter(lambda x: x % 2 == 0, lst))
print(evens)
