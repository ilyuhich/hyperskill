# отыскание суммы всех натуральных числел от 1 до введенного значения
# включительно при помощи классов


class NaturalNumber:

    def __init__(self, num):
        self.num = num
        self.numlist = [i for i in range(1, self.num + 1)]

    def count(self):
        print(self.numlist)
        print(sum(self.numlist))


number = NaturalNumber(int(input()))
number.count()
