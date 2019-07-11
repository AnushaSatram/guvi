pq=str(input())
cout=0
for h in range(0,len(pq)):
  if(pq[h].isalpha() or pq[h].isnumeric() or pq[h]==' ' or pq[h]=='.'):
    continue
  else:
    cout=cout+1
print(cout)
