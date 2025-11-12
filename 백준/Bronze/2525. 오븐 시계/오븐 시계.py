import sys
input = sys.stdin.readline

t, m = map(int, input().split(' '))
a = int(input())
tt = (t*60)+m+a
if tt>=60*24:
    tt-=60*24
print(str(tt//60)+' '+str(tt%60))