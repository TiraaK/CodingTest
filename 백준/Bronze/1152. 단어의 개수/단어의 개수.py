import sys
input = sys.stdin.readline
arr = list(map(str, input().strip().split(' ')))
if '' in arr:
    arr.remove("")
print(len(arr))
