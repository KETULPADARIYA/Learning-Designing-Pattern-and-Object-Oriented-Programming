class Mobile:
    brand = 'MI'

    @staticmethod
    def version(ver):
        print(Mobile.brand,"version is",ver)
        return ''


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
