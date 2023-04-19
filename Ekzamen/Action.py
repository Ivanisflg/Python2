class Action:
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
            f' === Action: {self.name} ===\n' \
            f' Здоровье: {self.health}\n' \
            f' Настроение: {self.sentiments}\n' \
            f' Деньги: {self.money}\n'