n = int(input())
r=[]

for i in input().split():
    x = int(i)
    r+=[x]
    
l=r
c=[]
m=0
b=r.count(1)

for i in range(b):
    if r[i]==0:m+=1
    
print(m)
