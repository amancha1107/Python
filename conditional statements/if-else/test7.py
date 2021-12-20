'''accept 3 subject marks from the user and findout, the student is pass or fail...pass marks are > 34 in all subjects'''

s1=int(input("enter subject1 marks: "))
s2=int(input("enter subject2 marks: "))
s3=int(input("enter subject3 marks: "))

if s1>34 and s2>34 and s3>34:
  print("pass")
else:
  print("fail")
