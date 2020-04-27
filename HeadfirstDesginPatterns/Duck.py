
class duck:
    """ Duck abstract class, because variable declaration cannot be done like java,
     so the value type is limited when changing attributes"""
    def __init__(self):
        self.quack = 'Quack Quack'
        self.display = "It's look like duck"
        self.swim = "It's good swimmer."


class redHeadDuck(duck):
    pass

class MalladDuck(duck):
    pass

