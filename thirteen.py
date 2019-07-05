digits=int(input())
if(digits>1):
  for i in range(2,digits):
    if(digits%2==0):
      print("no")
      break
    else:
      print("yes")
      break
else:
  print("no")
