class Mobile:

    brand = 'MI'

    @classmethod
    def version(cls,version_ = 'RealMe'):
        cls.version_ = version_
        cls.brand = 'Apple'
        print(cls.brand,"it's model:",version_)
        return  ''

    @classmethod
    def new_version(cls):
        print(cls.version_)



m = Mobile()
print(Mobile.version('I2'))
m.brand = 'oppo'
print(m.brand)
Mobile.brand = "Oppo"
print(m.brand)

print(m.version('I2'))
print(Mobile.version('I2'))

mm = Mobile()
print(mm.version('X1'))


mm.new_version()