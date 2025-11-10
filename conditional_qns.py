marks = int(input("Enter your Marks: "))
if ( marks >= 0 ) and ( marks <= 100 ) :
  if marks >= 90:
    print("A+")
  elif marks >= 80:
    print("A")
  elif marks >= 70:
    print("B+")
  elif marks >= 60:
    print("B")
  elif marks >= 50:
    print("C+")
  elif marks >= 40:
    print("C")
  else:
    print("Non - Graded")
else:
  print("Your Marks must be greater than 0 and less than equal to 100")
