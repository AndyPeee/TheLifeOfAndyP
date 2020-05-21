import math
import time

def modnar(range1, range2, digits):
    counter = 0
    x = int(range1)*math.pi
    y = int(range2)*math.e
    init_time = time.time()
    time.sleep(1)
    process = (abs(math.sin(x))*abs(math.sin(y)))/(x*y)
    after_time = time.time()
    time_diff = after_time-init_time
    dirty_int = time_diff*process
    clean(dirty_int, digits, range1, range2)

def clean(dirty_int, digits, range1, range2):
    counter = 0
    string = ""
    list = []
    final_list = []
    for x in str(dirty_int):
        list.append(x)
        list.reverse()
    list.remove("e")
    list.remove("-")
    list.remove(".")
    del list[0]
    while counter<int(digits):
       final_list.append(list[counter])
       counter = counter+1
    for e in final_list:
        string = string+str(e)
    if int(string)>=int(range1) and int(string)<=int(range2):
        print(string)
        return string
    else:
        modnar(range1, range2, digits)



range1 = input("Start of the range ")
range2 = input("End of the range ")
digits = len(str(range2))


modnar(range1, range2, digits)


