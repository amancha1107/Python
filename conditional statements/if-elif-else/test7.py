''' accept 3 subject marks and calculate total avg,resuilt and grade
pass marks are >34 in all subjects else fail
if avg>=70 print grade-A
if avg>=60 print grade-B
if avg>=50 print grade-C
else grade-D '''

s1=int(input("enter subject1 marks: "))
s2=int(input("enter subject2 marks: "))
s3=int(input("enter subject3 marks: "))

tot=s1+s2+s3
avg=tot/3
print("total is: ",tot)
print("average is: %.2f "%avg)
if s1>34 and s2>34 and s3>34:
    print("Result is pass")
    if avg>=70:
      print("grade-A")
    elif avg>=60:
      print("grade-B") 
    elif avg>=50:
      print("garde-C")
    else:
      print("grade-D")
else:
  print("fail")