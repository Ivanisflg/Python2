import random
import time


from Ekzamen.Person import Person
humans = []
human1 = Person(name = 'Тарас', health = 100, sentiments = 100, money = 200)
human2 = Person(name = 'Вася', health = 95, sentiments = 50, money = 1000)
human3 = Person(name = 'Петя', health = 97, sentiments = 75, money = 800)

humans.append(human1)
humans.append(human2)
humans.append(human3)
print(humans)
def work(human):
    human.change_state(
        money = random.randint(50, 100),
        sentiments = random.randint(-20, -10),
        health = random.randint(-10, -5)
    )


def rest(human):
    human.change_state(
        money = random.randint(-100, -50),
        sentiments = random.randint(10, 20),
        health = random.randint(5, 10)
    )


while True:
    for human in humans:
        try:
            work(human)
            print(f'Worked {human}')
            rest(human)
            print(f'Rested {human}')
        except Exception as exeption:
            break
            print(exeption)
        time.sleep(0.5)


