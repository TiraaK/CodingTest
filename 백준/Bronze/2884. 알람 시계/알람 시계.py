import sys
input = sys.stdin.readline

a, b = map(int, input().split(' '))
tt = a*60+b
t = (tt-45)//60
m = str((tt-45)%60)
print(str(t) if t >= 0 else str(t+24) ,m)