# PLay will role the dii
# Move the palyer through Board


class Player:
    def __init__(self, name):
        self.name = name
        self.current_position = 0

    @property
    def name(self):
        return self.name

    @property.setter
    def name(self, name):
        self.name = name

    @property
    def current_position(self):
        return self.current_position

    @property.setter
    def current_position(self, position):
        self.current_position = position

