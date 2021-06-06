class Car():
    '''Заводим машинку'''

    def __init__(self, color: str, name: str, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''

    def go(self, speed: float):
        ''' Начинает движение авто со скоростью'''
        try:
            self.speed = float(speed)
        except ValueError:
            pass

    def stop(self):
        """ Останавливает авто """
        self.speed = 0

    def turn(self, direction: str):
        ''' Поворот авто 'left', 'right' '''
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return

        if not self.speed:
            print(f"Can't turn to {direction} in place")
            return

        self._direction = direction

    def show_speed(self):
        ''' Показать текущуую скорость '''
        print(f'Car speed is {self.speed} km/h')

    def direction(self):
        ''' Показать текущее направление '''
        return self._direction


class TownCar(Car):
    '''Класс городских автомобилей '''
    _max_granted_speed = 60

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class SportCar(Car):
    '''Класс спортивный автомобилей '''

    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    """ Класс авто для работы """
    _max_granted_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_granted_speed:
            print('Over speed')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


cars_data = {
    ('Silver', 'Opel'): TownCar,
    ('Green', 'Lexus'): SportCar,
    ('White', 'Gazel'): WorkCar,
    ('Red', 'Ford'): PoliceCar,
}

for car_name, car_class in cars_data.items():
    car = car_class(*car_name)

    print(f"Car name {car.name}")
    print(f"Car color {car.color}")
    print(f"Car is police {car.is_police}")
    print(f"Car speed {car.speed}")
    print(f"Car direction {car.direction()}")
    print(f"Car show speed {car.show_speed()}")

    car.turn('right')
    car.go(30)
    car.turn('left')
    car.show_speed()
    car.go(45)
    car.show_speed()
    car.go(75)
    car.show_speed()
    car.turn('right')
    print(f"Car direction {car.direction()}")
    car.stop()
    car.show_speed()
    print('\n\n')
