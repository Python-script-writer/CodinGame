n = int(input())
mas=[]

for i in range(n):
    pi = int(input())
    
    mas.append(pi)
    
mas.sort()
delta = mas[0]
f = 0

for i in mas:
    if abs(i-f)<delta:
        delta=abs(i-f)
    f=i
    
print(delta)
