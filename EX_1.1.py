def Linear_Search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos

print(Linear_Search([7,10,12,14,16,20,29,37], 14))
print(Linear_Search([7,10,12,14,16,20,29,37], 29))