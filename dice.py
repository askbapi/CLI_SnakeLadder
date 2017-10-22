import random


class Die:
    def __init__(self, sides=1, *args, **kargs):
        self.sides = int(sides)

    def roll(self):
        return random.randrange(1, self.sides)


class DieSix(Die):
    def __init__(self, *args, **kargs):
        super().__init__(sides=6, *args, **kargs)

    def __str__(self):
        return 'The die have {} sides.'.format(self.sides)
