
class Person:
    name = ''
    health = 100
    sentiments = 0
    money = 0.0

    def __init__(self, name='', health=100, sentiments=0, money=0.0):
        self.name = name
        self.health = health
        self.sentiments = sentiments
        self.money = money


    def __str__(self):
        return \
            f' === {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настроение: {self.sentiments}\n' \
            f' Деньги: {self.money}\n'


    def change_state(self, health = 0, sentiments = 0, money = 0 ):
        self.health += health
        self.sentiments += sentiments
        self.money += money
        if self.health>100:
            self.health=100
        if self.health < 0:
            raise Exception("Человек скончался")
        if self.sentiments < 0:
            raise Exception('Человек впал в депрессию')
        if self.money < 0:
            raise Exception('Человек обанкротился')

    def do(self, action):
        print(action)
        self.change_state(health = action.health, sentiments = action.sentiments, money = action.money)






