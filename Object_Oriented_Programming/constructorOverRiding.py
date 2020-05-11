class Father:
    def __init__(self):
        self.money = 2009
        print("it's constructor of the Father Class")

    def show(self):
        print("it's method of Father Class",self.money)


class Child(Father):
    def __init__(self, money):
        # super().__init__(money)
        self.money = money
        print("it's constructor of the Child Class")

    def show_child(self):
        print("it's method of child Class")
        print()


child = Child(200)
child.show()