#if else

# accept a number from the user and findout the given number is positive or negative

n=int(input("enter a number: "))
if n>=0:
  print("number is positive")
else:
  print("number is negative")


print("+ve") if n>=0 else print("-ve")   #conditional operator