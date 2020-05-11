from Object_Oriented_Programming.classtools import AttrDisplay


class Person(AttrDisplay):
    """
    Create and Process person records.
    """

    def __init__(self,name,pay=1,job=None):

        self.name = name
        self.pay = pay
        self.job = job
    def lastName(self):
        return self.name.split()[-1]

    def giveRise(self,rise_percentage):
        self.pay =int(self.pay * (1+rise_percentage))

    # def __str__(self):
    #     return '[Person: %s %s]' % (self.name,self.pay)


class Manager(Person):
    """
    A customized Person with special arguments
    """
    def __init__(self,name,pay=1):
        super().__init__(name,pay,'mgr')


    def giveRise(self,rise_percentage,bonus_percentage=0.10):
        Person.giveRise(self,rise_percentage+bonus_percentage)


class Department:
    def __init__(self,*args):
        self.members = list(args)

    def addMember(self,person):
        self.members.append(person)

    def giveRise(self,percent):
        for object in self.members:
            object.giveRise(percent)

    def showAll(self):
        for member in self.members:
            print(member)







if __name__ == '__main__':
    bob = Person('Bob Smith')
    sui = Person('Sue Jones',pay= 100000,job='Developer')
    print(bob.name,bob.pay)
    print(bob)
    print(sui.name,sui.pay)
    print(sui)
    print(bob.lastName(),sui.lastName())

    tom = Manager('Tom Jones',pay=50000)
    tom.giveRise(.10)
    print(tom.lastName())
    print(tom)

    print("---ALL THREE ---")

    for object in [bob,sui,tom]:
        object.giveRise(.10)
        print(object)

    print('------Department-------21')

    department = Department(bob,sui)
    department.addMember(tom)
    department.showAll()
    department.giveRise(.10)
    department.showAll()