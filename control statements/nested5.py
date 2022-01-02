'''
1
1 *
1 * 3
1 * 3 *
1 * 3 * 5
'''

for i in range(1,6):
  for j in range(1,i+1):
    if j==2 or j==4:
      print("*",end=' ')
    else:
      print(j,end=" ")
  print(" ")