class Duck:
    def walk(self):
        print('thapak thapak thapak')

class Horse:
    def walk(self):
        print('thabdak thabdak thabdak')

class Cat:
    def talk(self):
        print('Mew Mew Mew')


def myfunction(obj):
    """if obj has walk method in that object then it will work"""
    obj.walk()

d = Duck()
h = Horse()

myfunction(d)
myfunction(h)

c = Cat()

try:
    myfunction(c)
except AttributeError as e:
    print(e)