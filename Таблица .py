class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_infoa(self):
        print(f'Brand: {self.brand} \nYear: {self.year}')


class Car(Vehicle):
    def __init__(self, brand, year, color):
        super().__init__(brand, year)
        self.color = color

    def display_infoa(self):
        super().display_infoa()
        print(f'Color: {self.color}')


class Motorcycle(Vehicle):
    def __init__(self, brand, year, speed):
        super().__init__(brand, year)
        self.speed = speed

    def display_infoa(self):
        super().display_infoa()
        print(f'Speed: {self.speed}')


a = Car('Nexia', 2023, 'Black')

a.display_infoa()
