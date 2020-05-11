from Object_Oriented_Programming.DesginingWithClass.employee import PizzaRobot,Server

class Customre:
    def __init__(self,name):
        self.name = name

    def order(self,server):
        print(self.name,"order from",server)

    def pay(self,server):
        print(self.name,"pay to",server)


class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.sever = Server("Pat")
        self.chef = PizzaRobot("Bob")
        self.oven = Oven()

    def order(self,name):
        customer = Customre(name)
        customer.order(self.sever)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.sever)


if __name__=="__main__":
    scene = PizzaShop()
    scene.order("Homer")
    print("...")
    scene.order("Shaggy")