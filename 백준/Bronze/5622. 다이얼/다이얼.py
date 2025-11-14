groups = ["ABC", "DEF", "GHI", "JKL", "MNO","PQRS", "TUV", "WXYZ"]
target = input()
sum = 0
for c in target:
    for i in range(len(groups)):
        if c in groups[i]:
            sum += i+3
print(sum)