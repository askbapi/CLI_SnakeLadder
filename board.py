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
        super().__init__(rows=rows, cols=cols)
        self.snakes = []
        self.ladder = []
        self.__set_snakes(snakes)
        self.__set_ladders(ladder)

    def draw(self):
        i = len(self.cells)
        for cell in range(self.rows):
            col_draw = ''
            for col in range(self.cols):
                col_draw += '[{:4d}] '.format(i)
                i -= 1

            print(col_draw)

    def __set_snakes(self, snakes=0):

        while len(self.snakes) <= snakes:
            # Last cell cannot have  snake head
            max_range = len(self.cells) - 1
            if max_range > (self.cols + 1):
                # Snake head cannot be on first row
                snakes_head = random.randrange(self.cols + 1, max_range)
                digit_list = list(str(snakes_head))

                # Tail should  not be in same row and show be below
                minimum_value = ((int(digit_list[0]) * 10) - 10)

                snakes_tail = random.randrange(2, snakes_head)
                if snakes_tail < minimum_value:
                    self.snakes.append([snakes_head, snakes_tail])

    def __set_ladders(self, ladder=0):

        while len(self.ladder) <= ladder:
            # Last cell cannot have  ladder head
            max_range = len(self.cells) - 10

            # Snake head cannot be on first row
            ladder_head = random.randrange(self.cols+1, max_range)
            digit_list = list(str(ladder_head))

            # Tail should  not be in same row and should be above
            if int(ladder_head) > 10:
                minimum_value = (int(digit_list[0]) * 10)
                ladder_tail = random.randrange(1, minimum_value)
                #if ladder_tail > minimum_value & ladder_head != ladder_tail:
                self.ladder.append([ladder_head, ladder_tail])


r = SnakeLadderBoard(5, 10, 5, 5)
print(r.cells)
print(r.snakes)
print(r.ladder)
