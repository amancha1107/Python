'''output:-
1
* *
3 3 3
* * * *
5 5 5 5 5
'''


for i in range(1,6):
    for j in range(1, i+1):
      if i==2 or i==4:
        print("*",end=' ')
      else:
        print(i,end=' ')
    print(" ")
