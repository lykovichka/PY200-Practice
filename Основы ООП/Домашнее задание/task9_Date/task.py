# TODO class Date
class Date:
    def __init__(self, day, month, year):
        if not isinstance(day, int):
            raise TypeError

        if not isinstance(month, int):
            raise TypeError

        if not isinstance(year, int):
            raise TypeError

        self.day = day
        self.month = month
        self.year = year

    def __repr__(self) -> str:
        return f"Date({self.day},{self.month},{self.year})"

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"

check = Date(11,02,2022)
print(check)

