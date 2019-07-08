w=int(input())
add=0
tp=w
while(tp>0):
  dig = tp%10
  add += dig**3
  tp //= 10
if(w==add):
  print("yes")
else:
  print("no")
