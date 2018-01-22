n = input()
print(min(input().split() or '0', key = lambda x: abs(int(x) - .1)))
