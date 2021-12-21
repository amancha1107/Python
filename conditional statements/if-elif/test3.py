''' accept 4 numbers from the user and print biggest number among them '''

a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
d=int(input("enter d number: "))

if a>b and a>c and a>d:
  print("a is big")
elif b>a and b>c and b>d:
  print("b is big")
elif c>a and c>b and c>d:
  print("c is big")
else:
  print("d is big")


#or
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
d=int(input("enter d number: "))

if a>b and a>c and a>d:
  print("a is big")
elif b>c and b>d:
  print("b is big")
elif c>d:
  print("c is big")
else:
  print("d is big")
