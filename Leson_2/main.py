from Lesson_4.charakter import Charakter
from colorama import Fore


player1 = Charakter(name='Ivan', health=70, damage=2,color=Fore.LIGHTWHITE_EX)
print(player1)

player2 = Charakter(name='Boss', health=100, damage=7,color=Fore.LIGHTWHITE_EX)
print(player2)


while player1.is_alive(True) and player2.is_alive(True):
    player2.attack(player1)
    player1.attack(player2)
    print(player1)
    print(player2)