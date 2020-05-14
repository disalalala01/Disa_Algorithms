


__all__ = [
    'Car',
]'''__all__ = [] Список в котором состоят импортируюмые объекты
тоесть объекты которым можно импортироватся
'''

class Car():


    def __init__(self, mark, model, year):

        self.mark = mark
        self.model = model
        self.year = year
        self.odometer = 0


    def description(self):
        desc = str(self.year) + " " + self.mark + " " + self.model

        return desc.title()


    def read_odometer(self):
        print( 'Пробег авто ' + str(self.odometer) + " km")


    def update_odometer(self, km):
        if km >= self.odometer:
            self.odometer = km
        else:
            print('No way bro')

    def increment_odometer(self, km):
        if km >= 0:
            self.odometer += km
        else:
            print( str(km) + ' < 0' )

#my_car = Car('audi', 'a6', 2010)
# print(my_car.description())
# my_car.update_odometer(114)
# my_car.update_odometer(100)
# my_car.increment_odometer(26)
# my_car.increment_odometer(-26)
# my_car.read_odometer()


class Battery():
    """Модель аккумулятора для электромобиля"""

    def __init__(self, battery=100):
        self.battery = battery


    def energy_battery(self):
        """Выводит информацию о мощности батареи"""
        print("Energy: " + str(self.battery) + 'kwt')


class ElectricCar(Car):
    """АСпекты для электромобиля"""


    def __init__(self, mark, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(mark, model, year)
        self.battery = Battery()


    def description(self):
        """Переопределение родительского метода"""
        desc = str(self.year) + " " + self.model
        return desc.title()

tesla = ElectricCar('tesla','model s',2017)
tesla.battery.energy_battery()
print(tesla.description())
