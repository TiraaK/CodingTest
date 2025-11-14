al = 'abcdefghijklmnopqrstuvwxyz'
list = [-1] * 26
target = input() 
for i, j in enumerate(target):
    for k, l in enumerate(al):
        if j == l and list[k] == -1:
            list[k] = i             
            break        
print(*list)