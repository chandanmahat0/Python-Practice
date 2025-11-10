def factorial(num):
  if num == 0 or num ==1:
     return 1;
  else:
      return num * factorial(num - 1);


num = int(input("Enter a number: "))
if num < 0:
    print("Negative number entered, factiorial is not defined.")
else:
   print("Factorial of",num,"is :",factorial(num))






