def topView(root):
    #Write your code here
    q = [(root,0,0)]
    m = dict()
    vh = 0
    while len(q) != 0:
        temp, hd, vh = q.pop(0)
        if hd in m.keys():
            m[hd].append((temp.info,vh))
        else:
            m[hd] = [(temp.info,vh)]
        if temp.left is not None:
            q.append((temp.left, hd-1, vh+1))
        if temp.right is not None:
            q.append((temp.right,hd+1, vh+1))
    
    # for key in sorted(m):
    #     print(m[key])
    m2 = dict()
    for key in sorted(m):
    #     max_vh = 0
    #     max_val = 0
        for val,vh in m[key]:
            if key in m2.keys():
                if vh < m2[key][1]:
                    m2[key] = (val,vh)
            else:
                m2[key] = (val,vh)
    
    for key in m2.keys():
        print(m2[key][0], end = ' ')
