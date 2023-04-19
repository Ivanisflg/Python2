import random
import time
from Ekzamen.Action import Action
from Ekzamen.Person import Person



human = Person(name = 'Тарас', money = 100, sentiments = 100, health = 100)
print(human)

go_to_work = Action(name = 'Отроботать робочий день', money = 59, sentiments = -5, health = -20)

go_to_cafe = Action(name = 'Сходить в кафе', money = -50, sentiments = 20, health = 7)

go_to_play = Action(name = 'Поиграть на компьютер', money = -40, sentiments = 20, health = -16)

go_to_park = Action(name = 'Сходить в аквопарк', money = -70, sentiments = 15, health = 10)

act = [go_to_cafe,go_to_play,go_to_park,go_to_work]

while True:
    human.do(random.choice(act))
    print(human)
    time.sleep(0.5)
