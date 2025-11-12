import sys
input = sys.stdin.readline
a, b, c = map(int, input().split(' '))
list = [a, b, c]

if len(set(list))==1:
    print(10000+a*1000)
elif len(set(list))==2:
    for i in list:
        if list.count(i)==2:               
            print(1000+i*100)
            break
else:
    list.sort()
    print(list[-1]*100)