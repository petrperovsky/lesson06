from time import sleep


class TrafficLight():
    '''Переключение цветов светофора 7 - 2 - 7 сек'''
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        for i in range(3):
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(7)


now_color = TrafficLight()
now_color.running()
