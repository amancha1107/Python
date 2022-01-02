
# for i  in range(3,10):
#   a=0
#   for j in range(2,i+1):
#     if i%j==0:
#       a=a+1
#   if a==1:
#      print(i,end=' ')

for i  in range(3,10):
  a=0
  for j in range(2,i):
    if i%j==0:
      a=a+1
  if a==0:
     print(i,end=' ')

