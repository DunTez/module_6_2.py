class Vehicle:
    def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color
        self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def print_info(self):
        print(f"Модель: {self.__model}, Мощность двигателя: {self.__engine_power}, "
              f"Цвет: {self.__color}, Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark 2', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('pink')
vehicle1.set_color('black')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
