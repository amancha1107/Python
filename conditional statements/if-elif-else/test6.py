#NESTED-IF

''' accept gender and age from the user and findout status of the candidate 
if gender is m|M then check the age if age>=21 print major else minor
if gender is f|F then check the age if age>=18 print major else minor
else third gender '''

gender=input("enter the gender m|M for male and f|F for female: ")
age=int(input("enter the age: "))
if gender in 'mM':
  if age>=21:
    print("major")
  else:
    print("minor")
elif gender in 'fF':
  if age>=18:
    print("major")
  else:
    print("minor")
else:
  print("third gender")