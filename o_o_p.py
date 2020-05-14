

class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        print("Собака создана")


    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " собака села")


    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыгнула")

my_dog = Dog('Aupau',2)
my_dog_al = Dog('Chetam', 4)
print(my_dog_al.name)
print(my_dog_al.age)
my_dog_al.sit()
my_dog_al.jump()
print(my_dog.age)
print(my_dog.name)
my_dog.jump()
my_dog.sit()
