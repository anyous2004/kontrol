#Задача 2

class Robot:

    def __init__(self, x, y):
        if 0 <= x <= 100:
            self.x = x
        else:
            print('Нельзя ставить такую координату, поэтому по икс у вас 0')
            self.x = 0

        if 0 <= y <= 100:
            self.y = y
        else:
            print('Нельзя ставить такую координату, поэтому по игрек у вас 0')
            self.y = 0

    def __str__(self):
        return f'Координаты робота сейчас: ({self.x}; {self.y})'

    def set_E(self):
        if 0 <= self.x <= 99:
            self.x += 1
        else:
            print('Достигнут максимум по икс')

    def set_W(self):
        if 1 <= self.x <= 100:
            self.x -= 1
        else:
            print('Достигнут минимум по икс')

    def set_N(self):
        if 0 <= self.y <= 99:
            self.y += 1
        else:
            print('Достигнут максимум по игрек')

    def set_S(self):
        if 1 <= self.y <= 100:
            self.y -= 1
        else:
            print('Достигнут минимум по игрек')


    def move(self, stroka):
        for letter in stroka:
            if letter == 'E':
                self.set_E()
            if letter == 'W':
                self.set_W()
            if letter == 'N':
                self.set_N()
            if letter == 'S':
                self.set_S()

        return f'Координаты робота после: ({self.x}; {self.y})'


def main():
    robot = Robot(890, -7)
    print(robot)
    print(robot.move('EEEEEEEEEEWWWNNNNNSS'))

    robot1 = Robot(58, 100)
    print(robot1)
    print(robot1.move('EEEEEEEEEEWWWNNNNNSS'))


main()




