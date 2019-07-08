digits=int(input())
if(digits>1):
  for p in range(2,digits):
    if((digits%p)==0):
      print("no")
      break
  else:
    print("yes")
else:
  print("no")
