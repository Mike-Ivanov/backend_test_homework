 

#from __future__ import annotations


class CarTracer:
    """Отслеживание автомобиля по номеру."""
    def __init__(self, number: int, position: Position) -> None:
        self.number = number
        self.position = position

    def __str__(self) -> str:
        return (f'Координаты автомобиля номер {self.number},: '
                f'{self.position.altitude}, {self.position.latitude}')

class Position:
    """Определяет широту и долготу."""
    def __init__(self, altitude: float, latitude: float) -> None:
        self.altitude = altitude
        self.latitude = latitude

moscow: Position = Position(55.7522, 37.6156)
car778: CarTracer = CarTracer(778, moscow)

print(car778)         