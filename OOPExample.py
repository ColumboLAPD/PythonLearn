# Introducing Python. Bill Lubanovic

# Task 10.4 - 10.8

class Element:
    def __init__(self, name, symbol, number):
        self.e_name = name
        self.e_symbol = symbol
        self.e_number = number

    @property
    def name(self):
        return self.e_name

    @property
    def symbol(self):
        return self.e_symbol

    @property
    def number(self):
        return self.e_number

    @name.setter
    def name(self, input_name):
        self.e_name = input_name

    @symbol.setter
    def symbol(self, input_symbol):
        self.e_symbol = input_symbol

    @number.setter
    def number(self, input_number):
        self.e_number = input_number

    def __str__(self):
        return f'name={self.name}, symbol={self.symbol}, number={self.number}'


element = Element('Hydrogen', 'H', 1)
elem_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
element1 = Element(elem_dict['name'], elem_dict['symbol'], elem_dict['number'])
hydrogen = Element('Hydrogen', 'H', 1)

print(element.name, element.symbol, element.number)
print(element1.name, element1.symbol, element1.number)
print(hydrogen)
# _____________________________________________________________________

# Task 10.9

class Animal:
    def __init__(self, name, eat):
        self.a_name = name
        self.a_eat = eat


class Bear(Animal):
    def __init__(self):
        super().__init__('Bear', 'berries')

    def eats(self):
        return f'{self.a_name} eat {self.a_eat}'


class Rabbit(Animal):
    def __init__(self):
        super().__init__('Rabbit', 'clover')

    def eats(self):
        return f'{self.a_name} eat {self.a_eat}'


class Octothorpe(Animal):
    def __init__(self):
        super().__init__('Octothorpe', 'campers')

    def eats(self):
        return f'{self.a_name} eat {self.a_eat}'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()
print(f'{bear.eats()}, {rabbit.eats()}, {octothorpe.eats()}')
# _____________________________________________________________________

# Task 10.10


class Laser:
    @staticmethod
    def does():
        return 'disintegrate'


class Claw:
    @staticmethod
    def does():
        return 'crush'


class SmartPhone:
    @staticmethod
    def does():
        return 'ring'


class Robot(Laser, Claw, SmartPhone):
    @staticmethod
    def does():
        laser = Laser.does()
        claw = Claw.does()
        smartphone = SmartPhone.does()

        print(f'laser-{laser}, claw-{claw}, smartphone-{smartphone}')


robot = Robot()
robot.does()




