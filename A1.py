def rvGroups(a, gs):
    tmp = 0
    ars = len(a)

    while tmp < ars:
        st = tmp
        end = min(tmp + gs-1, ars)
        while st < end:
            a[st], a[end] = a[end], a[st]
            st += 1
            end -= 1
        tmp += gs

a = [20, 30, 55, 66, 79, 90, 100, 0, 30]
rvGroups(a, 3)

for i in a: print(i)