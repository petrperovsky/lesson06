class Worker():
    '''Информация о работнике'''

    def __init__(self, name: str, surname: str, position: str, wage: float = 0, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    '''Класс позиции'''

    def get_full_name(self):
        return ' '.join([self.surname, self.name])

    def get_total_income(self):
        return (f'Доход: {sum(self._income.values())} rub')


worker_1 = Position('Petr', 'Perovsky', 'doctor')
print(worker_1.get_full_name(), worker_1.position, worker_1.get_total_income())
worker_2 = Position('Nata', 'Ivanova', 'president', 12500, 2300)
print(worker_2.get_full_name(), worker_2.position, worker_2.get_total_income())
