people = input("")
numberofinfected = input("")

rate = input("")
day = 0
while True:
    n = int(numberofinfected)
    if int(n) < int(people):
        day = day + 1
        numberofinfected = int(numberofinfected)*int(rate)
        if rate == 1:
            print(4)
            break
    else:
        print(day-1)
        break