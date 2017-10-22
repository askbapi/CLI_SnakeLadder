# Create diagram as per Row and Column
# show current position of a player


class Board:

    def __init__(self, rows=0, cols=0):
        self.rows = int(rows)
        self.cols = int(cols)
        self.cells = []
        for row in range(1, self.rows+1):
            cols_in_row = []
            for col in range(1, self.cols+1):
                cols_in_row.append(col)

            self.cells.append(cols_in_row)

    def __str__(self):
        return 'Board has {} rows and {} columns.'.format(self.rows, self.cols)