class Road():
    '''Расчет массы асфальта для дороги'''

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def mass(self):
        '''Масса дорожного покрытия толщиной в 5 см'''
        self.weight = 0.025
        self.thickness = 5
        try:
            return (f'Масса покрытия {self._length * self._width * self.weight * self.thickness} т')
        except TypeError:
            return None


road = Road(5000, 20)
print(road.mass())
