n = int(input())
q = int(input())
d={}


for i in range(n):
    e, m = input().split()
    d[e.lower()] = m
    
    
for i in range(q):
    f = input().lower().split(".")
    if f[-1] in d and len(f)>1:print(d[f[-1]])
    else:print("UNKNOWN")
