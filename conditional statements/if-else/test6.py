# accept a character from the user and find out the given char is vowel or not

n=input("enter a character: ")
if n=='a' or n=='A' or n=='e' or n=='E' or n=='i' or n=='I' or n=='o' or n=='O' or n=='u' or n=='U':
  print ("vowel")
else:
  print("not vowel")

print("=========================================")

  #or
lst=['a','A','e','E','i','I','o','O','u','U']        #list is iterable
n=input("enter a character: ")
if n in lst:
  print ("vowel")
else:
  print("not vowel")


print("=========================================")

#or
i="aAeEiIoOuU"       #string is also iterable
n=input("enter a character: ")
if i in lst:
  print ("vowel")
else:
  print("not vowel")