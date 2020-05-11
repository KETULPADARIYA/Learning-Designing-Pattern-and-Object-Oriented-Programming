class Employee:
    def __init__(self,name,salary= 0):
        self.name = name
        self.salary = salary

    def giveRise(self, percent):
        self.salary += self.salary*(1+percent)

    def work(self):
        print(self.name,"Does This")


    def __repr__(self):
        return "<Employee: name=%s, salary = %  s>" % (self.name,self.salary)


class Chef(Employee):
    def __init(self,name):
        Employee.__init__(self,name,50000)

    def work(self):
        print(self.name,"makes Food")


class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,40000)

    def work(self):
        print(self.name,"interfaces with customer")


class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print(self.name,"makes Pizza")



if __name__=="__main__":
    bob = PizzaRobot("bob")
    print(bob)
    bob.work()
    bob.giveRise(0.20)
    print(bob)
    print()

    for klass in Employee,Chef,Server,PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()