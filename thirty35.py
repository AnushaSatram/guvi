wq=str(input())
cnt=0
for b in range(0,len(wq)):
  if(wq[b].isnumeric()==True):
    cnt=cnt+1
print(cnt)
