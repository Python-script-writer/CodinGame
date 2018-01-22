n = int(input())
i = sorted(input().split())
if '-' in i:
    del(i[0])
    if i[0]=='.':
        if i[len(i)-1]=='0':
            print(0)
        else:
            print('-'+str(i[1])+'.'+''.join(i[2:]))
    else:
        print('-'+''.join(i[:]))

else:
    i.reverse()
    if i[len(i)-1]=='.':
        if i[len(i)-2]=='0':
            print(''.join(i[:len(i)-2]))
        else:
            print(''.join(i[:len(i)-2])+'.'+str(i[len(i)-2]))
    else:
        print(''.join(i[:len(i)]))
