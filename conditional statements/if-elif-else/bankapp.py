oldbal=int(input("enter your old balance: "))
ttype=input("enter transaction type either w|W or d|D: ")
tamt=int(input("enter transaction amount: "))
lst=['w','W','d','D']

#if ttype=='w' or ttype=='W':       #withdraw
#if ttype in 'wW'
if ttype in lst[0:2:1]:
   if tamt>oldbal:
     print("insufficient funds")
   elif tamt==oldbal:
     print("please maintain minimum balance")
   else:
     cbal=oldbal-tamt
     print("current balance is: ",cbal)
elif ttype in lst[2:4:1]:                          #deposit
   if tamt>=50000:
     print("Required PAN card")
   else:
     cbal=oldbal+tamt
     print("Current balance is: ",cbal)
else:
  print("Invalid ")