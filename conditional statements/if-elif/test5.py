''' accept any character from the user and print male if the given char is m|M, print female if the given char is f|F else print third gender '''

gender=input("enter any character: ")
if gender in 'mM':
  print("male")
elif gender in 'fF':
  print("female")
else:
  print("third gender")