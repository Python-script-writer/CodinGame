print(sorted(map(int, input().split()), key = lambda x: (x**2,-x))[0] if int(input()) else 0)
