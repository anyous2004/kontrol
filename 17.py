class Person:
    def __init__(self, name, age):
        if name != 'Олег':
            print(f'Я не {name}, а Олег')
        self._name = 'Олег'
        self.age = age

pers = Person('Олег', 19)
print('сверху должно быть ничего, а снизу вот:')
pers1 = Person('МПОГМАОГЛ', 45)
pers2 = Person('олег', 87)

