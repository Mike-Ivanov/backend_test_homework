from dataclasses import dataclass
from typing import Type, Dict


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float

    def get_message(self) -> str:
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; '
                f'Ср. скорость: {self.speed:.3f} км/ч; '
                f'Потрачено ккал: {self.calories:.3f}.'
                )


class Training:
    """Базовый класс тренировки."""
    M_IN_KM: float = 1000
    LEN_STEP: float = 0.65

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        information_message = InfoMessage(type(self).__name__,
                                          self.duration,
                                          self.get_distance(),
                                          self.get_mean_speed(),
                                          self.get_spent_calories()
                                          )
        return information_message


class Running(Training):
    """Тренировка: бег."""
    CAL_RUN_1: int = 18
    CAL_RUN_2: int = 20

    def get_spent_calories(self) -> float:
        return ((self.CAL_RUN_1 * self.get_mean_speed() - self.CAL_RUN_2)
                * self.weight / Training.M_IN_KM * self.duration * 60)


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CAL_WALK_1: float = 0.035
    CAL_WALK_2: float = 0.029
    MIN_IN_HOUR: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        return ((self.CAL_WALK_1 * self.weight
                 + (self.get_mean_speed()**2 // self.height)
                 * self.CAL_WALK_2 * self.weight)
                * (self.duration * self.MIN_IN_HOUR))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    CAL_SWM_1: float = 1.1
    CAL_SWM_2: int = 2

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ):
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return (self.length_pool * self.count_pool / Training.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + Swimming.CAL_SWM_1)
                * Swimming.CAL_SWM_2 * self.weight)


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    all_trainings: Dict[str, Type[Training]] = {'RUN': Running,
                                                'WLK': SportsWalking,
                                                'SWM': Swimming
                                                }
    return all_trainings[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)