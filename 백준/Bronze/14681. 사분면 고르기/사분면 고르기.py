import sys
input = sys.stdin.readline

a, b = int(input()), int(input())
print(1 if a>0 and b>0 else 2 if a<0 and b>0 else 3 if a<0 and b<0 else 4)