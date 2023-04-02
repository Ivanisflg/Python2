from colorama import Fore, Style
import datetime


class Student:

    name = ''
    birth_year = 0
    team = 0
    ball = 0
    color = Fore.LIGHTGREEN_EX

    def __init__(self, name='', birth_year=0, team=0, ball=0, color=Fore.LIGHTWHITE_EX):
        self.name = name
        self.birth_year = birth_year
        self.team = team
        self.ball = ball
        self.color = color

    def get_age(self):
        return (datetime.date.today().year-self.birth_year)

    def __str__(self):
        return self.get_stars()

    def get_stars(self):
        return  \
            f'{self.color}' \
            f'Имя: {self.name}\n' \
            f'Год рождения: {self.birth_year}\n' \
            f'Возраст: {self.get_age()}\n' \
            f'Группа: {self.team}\n' \
            f'Средний бал: {self.ball}\n' \
            f'{Style.RESET_ALL}'