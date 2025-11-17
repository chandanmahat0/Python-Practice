# 19. Remove None values from user list.
lst = eval(input("Enter list: "))
clean = [x for x in lst if x is not None]
print(clean)
