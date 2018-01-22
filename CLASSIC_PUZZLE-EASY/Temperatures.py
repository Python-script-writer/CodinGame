r=5526
if int(input())==0:r=0

for i in input().split():
    t = int(i)
    if abs(r)>abs(t):r=t
    if abs(r)==abs(t) and r!=t:r=abs(t)

print(r)
