from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        #  TODO инициализировать объект "Стакан"
        if isinstance(capacity_volume,(int, float)) != True:
            raise TypeError
        if isinstance(occupied_volume,(int, float)) != True:
            raise TypeError
        if capacity_volume < 0 or occupied_volume < 0:
            raise ValueError
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    ...  # TODO инициализировать два объекта типа Glass
    glass_1 = Glass(500,200)
    glass_2 = Glass(200,150)
    # TODO попробовать инициализировать не корректные объекты
    glass_3 = Glass(-2, 0)
    glass_4 = Glass(-3,-5)