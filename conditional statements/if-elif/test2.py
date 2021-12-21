''' accept a character from the user and print colour name
if char is g|G print green
if char is b|B print blue
if char is r|R print red '''

n=input("enter a char: ")
if n=='g'or n=='G':
  print("green")
elif n=='b' or n=='B':
  print("blue")
elif n=='r' or n=='R':
  print("red")
else:
  print("invalid")


#or

n=input("enter a char: ")
lst=['g','G','b','B','r','R']
if n in lst[0:2:1]:
  print("green")
elif n in lst[2:4:1]:
  print("blue")
elif n in lst[4:6:1]:
  print("red")
else:
  print("invalid")