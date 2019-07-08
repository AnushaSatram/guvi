dg=int(input())
kg=int(input())
for p in range(dg+1,kg):
  if(p>1):
    for x in range(2,p):
      if((p%x)==0):
        break
    else:
      print(p,end = ' ')
