dropsofpaint = int(input(""))
xlist = []
ylist = []
for f in range(dropsofpaint):
    comma = False
    holderx = ""
    holdery = ""
    coordinate = input("")
    for e in coordinate:
        if e == ",":
            comma = True
        if not comma:
            holderx = holderx+e
        else:
            if e != ",":
                holdery = holdery+e
    xlist.append(int(holderx))
    ylist.append(int(holdery))
xlist.sort()
ylist.sort()
print(str((int(xlist[0])-1))+str(",")+str((int(ylist[0])-1)))
print(str((int(xlist[-1])+1))+str(",")+str((int(ylist[-1])+1)))