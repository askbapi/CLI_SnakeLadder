# Create diagram as per Row and Column
# draw board
# list of snake head and tail. Snake head cannot be on 1 and 100
# list of Ladder head and tail. Snake head cannot be on 1 and 100
# show current position of a player
import random

class Board:

    def __init__(self, rows=0, cols=0):
        self.rows = int(rows)
        self.cols = int(cols)
        self.cells = list(range(1, (self.rows*self.cols)+1))


    def __str__(self):
        return 'Board has {} rows and {} columns.'.format(self.rows, self.cols)


class SnakeLadderBoard(Board):
    def __init__(self, rows=0, cols=0, snakes=0, ladder=0):
        super().__init__(rows=10, cols=10)

        self.snakes = []
        for snk in range(snakes):
            self.snakes.append(random.random(2, len(self.cells)-1))
        self.ladders = []

    def draw(self):
        i = 100
        for row in range(self.rows):
            col_draw = ''
            for col in range(self.cols):
                col_draw += '[{:4d}] '.format(i)
                i -= 1

            print(col_draw)