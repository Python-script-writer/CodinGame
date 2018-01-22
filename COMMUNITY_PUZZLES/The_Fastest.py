n = int(input())
c=[]
for i in range(n):
    t = input()
    c+=[t]

m=24*60*60
l=0

for i in range(len(c)):
    if int(c[i].split(":")[0])*60*60+int(c[i].split(":")[1])*60+int(c[i].split(":")[2])<m:
        m=int(c[i].split(":")[0])*60*60+int(c[i].split(":")[1])*60+int(c[i].split(":")[2])
        l=c[i]
print(l)
