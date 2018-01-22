for i in range(int(input())):
    land_x, land_y = [int(j) for j in input().split()]


while True:
    x, y, h, v, f, r, p = [int(i) for i in input().split()]
    if v<=-40:print("0 4")
    else:print("0 0")
