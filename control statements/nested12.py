lst=[10,20,30,40,50]
print("lst is: ",lst)
element=int(input("enter an element to search: "))
for i in lst:
  if element==i:
    print("element is present in the list")
    break
else:
  print('element is not found in the list')