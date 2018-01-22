while True:
    S={}
    for i in range(8):
        mountain_h = int(input())
        S[i]=mountain_h
    L=sorted(S.items(), key=lambda t: t[1])
    print(L[len(L)-1][0])
    S.clear()
    L.clear()
