new=[]
nun=int(input())
kin=int(input())
added=0
for a in range(nun):
  ssm=int(input())
  new.append(ssm)
for d in range(0,kin):
  added=added+new[d]
print(added)
