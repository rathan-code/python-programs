 ta = to = 0
    for i in range(len(apples)):
        if s<= a + apples[i] <=t :
            ta+=1
    for i in range(len(oranges)):
        if s<= b+oranges[i] <=t:
            to+=1
    print(ta)
    print(to)