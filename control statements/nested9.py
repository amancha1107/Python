'''
1 2 3
4 5 6
7 8 9 
'''
i=1
while i <= 9:
    for a in range(3):
       print(i,end=" ")
       i=i+1
    print()


print("="*5)


i=1
for j in range(3):
  for k in range(3):
    print(i,end=" ")
    i=i+1
  print()
