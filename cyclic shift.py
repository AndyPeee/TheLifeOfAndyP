text = input("text")
string = input("string")
shifts = []
shifting = []
holder = ""
finalstr = ""
shifts.append(text)
length = len(text)
firstime = True
newtext = text
def move():
    holder = shifting.pop(0)
    shifting.append(holder)


for e in range(length-1):
    shifting = []
    for w in newtext:
        shifting.append(w)
    move()
    print(shifting)
    shifts.append(shifting)
    print(shifts)