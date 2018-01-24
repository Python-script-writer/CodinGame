l = int(input())
h = int(input())
t = input()
c=[]


for i in t:
    if 64 < ord(i) < 91:c += [ord(i)-64]
    elif 96 < ord(i) < 123:c += [ord(i)-96]
    else:c += [91-64]
    
    
for i in range(h):
    row = input()
    for j in c[:-1]:
        print(row[(j-1)*l:j*(l)],end = '')
    print(row[(c[-1]-1)*l:c[-1]*(l)])
