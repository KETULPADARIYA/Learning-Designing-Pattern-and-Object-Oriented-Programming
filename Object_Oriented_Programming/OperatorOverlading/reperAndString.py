class adder:
    def __init__(self,value = 0):
        self.data = value

    def __add__(self, other):
        return  adder(self.data + other)

x = adder()

def printStrAndprintReper(x):
    print(x)
    print(repr(x))

printStrAndprintReper(x)

class addreper(adder):
    def __repr__(self):
        return  " addreper(%s)" %self.data

printStrAndprintReper(addreper())

class addstr(adder):
    def __str__(self):
        return  " addstr(%s)" %self.data

l = addstr(3)

printStrAndprintReper(l  )

class addboth(adder):
    def __str__(self):
        return "[Value: %s ]" % self.data

    def __repr__(self):
        return "addboth(%s)" % self.data

printStrAndprintReper(addboth(2))


class Printer:
    def __init__(self,v):
        self.value = v

    def __str__(self):
        return str(self.value)

objs = [Printer(2),Printer(3)]
for x in objs:
    print(x)

print(objs)


class PrinterModified(Printer):
    def __repr__(self):
        return str(self.value)

objs = [PrinterModified(2),PrinterModified(3)]

for x in objs:
    print(x)

print(objs)
