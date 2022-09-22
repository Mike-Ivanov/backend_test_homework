
class Running():
    def __init__(self,
                a,
                b,
                c,
                d
                ) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def printing_my_class(self):
        print(f'{self.a}, {self.b}, {self.c}, {self.d}')    

my_list = (1, 2, 3, 4)

# for name, val in your_list:
#     globals()[name] = your_class(val)

my_obj = Running(my_list[0], my_list[1], my_list[2], my_list[3])

Running.printing_my_class(my_obj)

class InfoMessage:
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories
    def get_message(self) -> str:
        """Возвращает информационное сообщение о тренировке."""
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.')
