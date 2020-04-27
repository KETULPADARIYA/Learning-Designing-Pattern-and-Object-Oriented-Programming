from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        print('It is processing')


try:
    cp = Computer()
except TypeError as e:
    print(e)


class laptop(Computer):
    pass


try:
    lp = laptop()
except TypeError as e:
    print(e)


class Desktop(Computer):
    def process(self):
        print('Desktop Process is running')


dsp = Desktop().process()


# We can define concrete method also here.
class Computer(ABC):
    @abstractmethod
    def process(self):
        print('It is processing')

    def speed(self):
        print('It"s speedy')
        return 'Speed'


class Desktop(Computer):
    def process(self):
        print('Desktop Process is running')
        return '....'


dsp = Desktop()
print('DESKTOP PROCESS', dsp.process())
print('DESKTOP SPEED', dsp.speed())
