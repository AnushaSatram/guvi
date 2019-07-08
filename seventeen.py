w=int(input())
add=0
tp=w
while(tp>0):
  w = tp%10
  add += w**3
  tp //= 10
if(w==add):
  print("yes")
else:
  print("no")
