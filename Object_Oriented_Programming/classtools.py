"""  Asserted Class utility and tools. """

class AttrDisplay:
    """
    Provides an inheritable print overload method that displays
    instances with their class names  and name values  pair for
    each attributes stored on the instance itself (but not
    attribute inherited from its classes). Can be mixed into any
    class and will work on any instance.
    """

    def gatherAttrs(self):

        return ' , '.join('%s = %s' % (key,getattr(self,key))  for key in sorted(self.__dict__) )


    def __str__(self):
        return '[%s:%s]' %(self.__class__.__name__,self.gatherAttrs())


if __name__ =='__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count +1
            self.attr2 = TopTest.count + 2
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X,Y = TopTest(),SubTest()
    print(X)
    print(Y)