def leaders(a):
    l = len(a)
    cmax = a[l-1]
    print(cmax)
    
    for i in range(l-2, -1, -1):
        if cmax < a[i]:
            cmax = a[i]
            print(cmax)


a = [16, 17, 18, 20, 21, 245]
leaders(a)