from typing import Union


# TODO Добавить методы add_water и remove_water
class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

    def init_capacity_volume(self, capacity_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if self.occupied_volume + water > self.capacity_volume:
            raise ValueError
        self.occupied_volume += water
        return self.occupied_volume

    def remove_water(self, del_water):

        if self.occupied_volume - del_water < 0:
            raise ValueError('vbyec')
        self.occupied_volume -= del_water
        return self.occupied_volume


if __name__ == "__main__":
    glass = Glass(800, 100)  # экземпляр класса
    print(glass.add_water(500))
    print(glass.remove_water(300))
    print(glass.capacity_volume, glass.occupied_volume)
