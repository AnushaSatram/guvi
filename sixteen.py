d,k=map(int,input().split())
for p in range(d+1,k):
    for x in range(2,p):
        if(p%x==0):
            break
    else:
        print(p,end =" ")
