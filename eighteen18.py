m,n=map(int,input().split())
for x in range(m+1,n):
  ol = len(str(x))
  add=0
  tp=x
  while(tp>0):
    dg = tp%10
    add += dg**ol
    tp //=10
  
  if(x==add):
    print(x,end = " ")
