w, h = [int(i) for i in input().split()]
l=[]
for i in range(h):
    line = input().split()
    l+=[line]
ex = int(input())

def t0():return 0
    
    
def t1():return str(x)+' '+str(y+1)
    
    
def t2():
    if pos=="LEFT":
        return str(x+1)+' '+str(y)
    if pos=="RIGHT":
        return str(x-1)+' '+str(y)


def t3():
    return str(x)+' '+str(y+1)


def t4():
    if pos=="TOP":
        return str(x-1)+' '+str(y)
    if pos=="RIGHT":
        return str(x)+' '+str(y+1)


def t5():
    if pos=="TOP":
        return str(x+1)+' '+str(y)
    if pos=="LEFT":
        return str(x)+' '+str(y+1)


def t6():
    if pos=="LEFT":
        return str(x+1)+' '+str(y)
    if pos=="RIGHT":
        return str(x-1)+' '+str(y)


def t7():
    return str(x)+' '+str(y+1)
    
    
def t8():
    if pos=="LEFT":
        return str(x)+' '+str(y+1)
    if pos=="RIGHT":
        return str(x)+' '+str(y+1)
        

def t9():
    return str(x)+' '+str(y+1)
        
        
def t10():
     return str(x-1)+' '+str(y)


def t11():
    return str(x+1)+' '+str(y)
    
    
def t12():
    return str(x)+' '+str(y+1)
    
    
def t13():
    return str(x)+' '+str(y+1)


while True:
    x, y, pos = input().split()
    x = int(x)
    y = int(y)
    if l[y][x]=='1':print(t1())
    if l[y][x]=='2':print(t2())
    if l[y][x]=='3':print(t3())
    if l[y][x]=='4':print(t4())
    if l[y][x]=='5':print(t5())
    if l[y][x]=='6':print(t6())
    if l[y][x]=='7':print(t7())
    if l[y][x]=='8':print(t8())
    if l[y][x]=='9':print(t9())
    if l[y][x]=='10':print(t10())
    if l[y][x]=='11':print(t11())
    if l[y][x]=='12':print(t12())
    if l[y][x]=='13':print(t13())
