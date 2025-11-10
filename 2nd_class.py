number_1 = int(input("Enter Marks out of 100: "))
if number_1>=0 and number_1<100:
    
    if number_1 >= 90 and number_1<100:
        print(number_1,"Grade is A+")
        
    elif number_1 >= 80 and number_1 < 90:
        print(number_1,"Grade is A")
        
    elif number_1 >= 70 and number_1 < 80:
        print(number_1,"Grade is B+")
        
    elif number_1 >= 60 and number_1 < 70:
        print(number_1,"Grade is B")
        
    elif number_1 >= 50 and number_1 < 60:
        print(number_1,"Grade is C+")
        
    elif number_1 >= 40 and number_1 < 50:
        print(number_1,"Grade is C")
        
    elif number_1 >= 30 and number_1 < 40:
        print(number_1,"Grade is D+")
        
    elif number_1 >= 20 and number_1 < 30:
        print(number_1,"Grade is D")
        
    else:
        print(number_1,"Non-Graded")

elif number_1<0:
    print(number_1,"Given input is less than 0")

else:
    print(number_1,"Given input is greater than 100")
            
               
