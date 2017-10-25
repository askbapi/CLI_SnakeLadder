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
        self.cells = {}
        for cell_no in range(1, (self.rows * self.cols) + 1):
            self.cells[cell_no] = ' [{:5d}] '.format(cell_no)

    def __str__(self):
        return 'Board has {} rows and {} columns.'.format(self.rows, self.cols)


class SnakeLadderBoard(Board):
    def __init__(self, rows=0, cols=0, snakes=0, ladder=0, **kwarg):
        super().__init__(rows=rows, cols=cols)
        self.snakes_head = []
        self.snakes_tail = []
        self.ladder_head = []
        self.ladder_tail = []
        self.__set_snakes(snakes)
        self.__set_ladders(ladder)

    def __set_snakes(self, snakes=0):
        while len(self.snakes_head) <= snakes:
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
                    self.snakes_head.append(snakes_head)
                    self.snakes_tail.append(snakes_tail)

    def __set_ladders(self, ladder=0):
        while len(self.ladder_head) <= ladder:
            # Last cell cannot have  ladder head
            max_range = len(self.cells) - 10

            # Snake head cannot be on first row
            ladder_head = random.randrange(self.cols + 1, max_range)
            digit_list = list(str(ladder_head))

            # Tail should  not be in same row and should be above
            if int(ladder_head) > 10:
                minimum_value = (int(digit_list[0]) * 10)
                ladder_tail = random.randrange(1, minimum_value)
                # if ladder_tail > minimum_value & ladder_head != ladder_tail:
                if ladder_head not in self.snakes_head:
                    self.ladder_head.append(ladder_head)

                if ladder_tail not in self.snakes_tail:
                    self.ladder_tail.append(ladder_tail)

    def draw(self, pointers):
        print('=' * 100)

        i = 1
        col_draw = ''
        for cell, cell_value in self.cells.items():
            # Adding Snake Head
            if cell in self.snakes_head:
                if cell in pointers.keys():
                    self.cells[cell] = '[-<{:3d} {}]'.format(cell, pointers[cell])
                else:
                    self.cells[cell] = '[-<{:3d}]'.format(cell)

            # Adding Snake Tail
            elif cell in self.snakes_tail:
                if cell in pointers.keys():
                    self.cells[cell] = '[-<{:3d} {}]'.format(cell, pointers[cell])
                else:
                    self.cells[cell] = '[-<{:3d}]'.format(cell)

            # Adding Ladder Head
            elif cell in self.ladder_head:
                if cell in pointers.keys():
                    self.cells[cell] = '[-<{:3d} {}]'.format(cell, pointers[cell])
                else:
                    self.cells[cell] = '[-<{:3d}]'.format(cell)

            # Adding Ladder Tail
            elif cell in self.ladder_tail:
                if cell in pointers.keys():
                    self.cells[cell] = '[H{:4d} {}]'.format(cell, pointers[cell])
                else:
                    self.cells[cell] = '[H{:4d}]'.format(cell)

            if cell in pointers.keys():
                self.cells[cell] = '[-<{:3d} {}]'.format(cell, pointers[cell])

            col_draw += self.cells[cell]
            if i >= 10:
                i = 0
                print("|    " + col_draw + "   |")
                col_draw = ''

            i += 1
        print('=' * 100)



