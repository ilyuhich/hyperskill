# отыскание текущего состояния копилки:
# в копилке лежит сумма в долларах и центах
# при добавлении нужно учитывать что центов может быть не более 99


class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, doll, cent):
        self.dollars = doll
        self.cents = cent

    def add_money(self, deposit_dollars, deposit_cents):
        cents = self.cents + self.dollars * 100 + deposit_cents + deposit_dollars * 100
        self.dollars = cents // 100
        self.cents = cents - self.dollars * 100
        #print(f"{self.dollars} {self.cents}")


# основная программа
# создание экземпляра класса
#pig = PiggyBank(1, 1)
# получаем значения вносимых денег в строку через пробел
#doll, cent = input().split()
#doll, cent = int(doll), int(cent)
# вызываем метод добавления денег
#pig.add_money(doll, cent)