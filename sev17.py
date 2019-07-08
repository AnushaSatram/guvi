wp=int(input())
add=0
tp=wp
while(tp>0):
  dig = tp%10
  add += dig**3
  tp //= 10
if(wp==add):
  print("yes")
else:
  print("no")
