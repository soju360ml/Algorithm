def bs(baselist, target, l, r):
    center = (l + r) // 2
    
    while True:
        if baselist[center] == target:
            return target