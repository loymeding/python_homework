'''
Создайте класс Animal с атрибутами name и sound, и методом makesound(),
который будет выводить на экран звук животного. Создайте объекты Cat и Dog,
которые будут наследоваться от класса Animal и иметь дополнительный атрибут color.
Переопределите метод makesound() для каждого подкласса, чтобы он выводил на экран соответствующий звук.
'''


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} говорит: {self.sound}")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу")
        self.color = color

    def make_sound(self):
        print(f"{self.name} (цвет: {self.color}) говорит: {self.sound}")


class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав")
        self.color = color

    def make_sound(self):
        print(f"{self.name} (цвет: {self.color}) говорит: {self.sound}")


# Примеры использования
cat = Cat("Мурка", "Черный")
dog = Dog("Шарик", "Коричневый")

cat.make_sound()
dog.make_sound()
