def rots(a, n):
    for i in range(n): rot(a)

def rot(a):
    al = len(a)
    t = a[0]
    for i in range(al-1):
        a[i] = a[i+1]
    a[al-1] = t

def retArr(a):
    buffer = ""
    l = len(a)
    for i in range(l): buffer += "% d"%a[i]
    buffer += '\n'
    return buffer

a = [12, 12, 13, 15, 37, 29, 1, 0, 64552]
print(retArr(a))
rots(a, 2)
print(retArr(a))
