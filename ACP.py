from math import floor as fl

def missing(a):
    l = len(a)
    t = (l+1) * (l+2) / 2
    s = sum(a)
    if fl(t) == t: t = int(t)
    return t - s

arr = [2, 3, 4]

print(f"The missing number from", arr, "is", missing(arr))