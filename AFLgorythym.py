class Stack:
    def __init__(self):
        self.list = []
    def pop(self):
        return self.list.pop()
    def push(self, x):
        self.list.append(x)
    def length(self):
        return len(self.list)
    def peek(self):
        return self.list[-1]


class Queue:
    def __init__(self):
        self.list = []
    def equeue(self):
        self.list.append(x)
    def dequeue(self):
        holder = self.list[0]
        del self.list[0]
        return holder
    def length(self):
        return len(self.list)
    def peek(self):
        return self.list[0]


stack = Stack()


#1 write a recurssive function that will find the amount of 5's in a given number
fivelist = []
e = input("num ")
for x in e:
    stack.push(x)


def fives():
    if stack.length() > 0:
        holder = int(stack.pop())
        if holder == 5:
            fivelist.append(holder)
        fives()
    else:
        print(len(fivelist))


fives()


#2 Write a recursive function called repeatStrings(string, num) that returns a concatenation of the string repeated num times.
# If num = 0, the function should return an empty string

string = input("string ")
num = int(input("num "))


def repeatedStrings(string, num):
    if num == 0:
        return ""
    elif num == 1:
        return string
    else:
        num = num-1
        return repeatedStrings(string, num) + string


print(repeatedStrings(string, num))

#3 Write a recursive function called onlyEven(numList) that will return a list of only
# even numbers from numList in descending order.
r = input("nums ")
evenlist = []
finalist = []
for w in r:
    stack.push(w)


def onlyEven():
    if stack.length() == 0:
        for repeating in range(len(evenlist)):
            finalist.append(max(evenlist))
            evenlist.remove(max(evenlist))
        print(finalist)
    else:
        holder = stack.pop()
        if int(holder) % 2 == 0:
            evenlist.append(int(holder))
        onlyEven()


onlyEven()

#Write a function reverseString(str) that will use a Stack to return a string that is the reverse of the parameter str.
str = input("string pls ")
for q in str:
    stack.push(q)
finalstring = ""

def reverseString(finalstring):
    if stack.length() == 0:
        print(finalstring)
    else:
        stack.peek()
        holder = stack.pop()
        finalstring = finalstring + holder
        reverseString(finalstring)


reverseString(finalstring)


#Write a function using an ADT of your choice (it may be more than one),
# that will check if a string has completely balanced brackets – for all types of brackts – (), [], {}


class Bracket:
    def __init__(self):
        self.dict = {"{": 0, "}": 0, "[": 0, "]": 0, "(": 0, ")": 0}
    def add(self,checker):
        self.dict[checker] += 1
    def checkem(self, r):
        for checker in r:
            if checker == "[" or checker == "]" or checker == "{" or checker == "}" or checker == "(" or checker == ")":
                bracket.add(checker)
    def balancem(self):
        if self.dict["{"] == self.dict["}"] and self.dict["["] == self.dict["]"] and self.dict["("] == self.dict[")"]:
            print("its balanced")
        else:
            print("fix it")
    def view(self):
        print(self.dict)


bracket = Bracket()

r = input("BRACKETS PLS ")

bracket.checkem(r)
bracket.balancem()
