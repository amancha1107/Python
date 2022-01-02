m=7
for i in range(1,m+1):   #1234
 if i%2!=0:
    print(' '*m,end=' ')
    print('* '*i)
    m=m-1
 else:
   m=m+1
