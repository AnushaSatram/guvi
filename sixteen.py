dg,kg=map(int,input().split())
for p in range(dg+1,kg):
    for x in range(2,p):
      if((p%x)==0):
        break
    else:
      print(p,end = ' ')
