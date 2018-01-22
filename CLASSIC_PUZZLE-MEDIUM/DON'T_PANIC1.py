c=[int(i) for i in input().split()]
s=[]
for i in range(c[-1]):s+=[[int(j) for j in input().split()]]
s.sort()
while True:
 f,p,d=input().split()
 f=int(f)
 p=int(p)
 try:print("BLOCK" if s[f][1]<p and d=='RIGHT'or s[f][1]>p and d=='LEFT'else"WAIT")
 except:
  if c[4]<p and d=='RIGHT'or c[4]>p and d=='LEFT':print("BLOCK")
  print("WAIT")
