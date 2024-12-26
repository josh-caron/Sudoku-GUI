import random


class SudokuGenerator:
    def __init__(self, row_length=9, removed_cells=30):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0] * row_length for _ in range(row_length)]

    def get_board(self):
        # Return the board
        return self.board

    def valid_in_row(self, row, num):
        # Check if the number is not in the row
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Check if the number is not in the column
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        # Checks if the number is not in the 3x3 box
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # Check if num is valid for the 3x3 box
        box_row = row - row % 3
        box_col = col - col % 3
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(box_row, box_col, num))

    def fill_box(self, row_start, col_start):
        # Fill a 3x3 box with random numbers
        nums = random.sample(range(1, 10), 9)
        for i in range(3):
            for j in range(3):
                self.board[row_start + i][col_start + j] = nums.pop()

    def fill_diagonal(self):
        # Fill the diagonal boxes
        for i in range(0, self.row_length, 3):
            self.fill_box(i, i)

    def fill_remaining(self, row=0, col=0):
        # Fill the rest with the board
        if col >= self.row_length:
            row += 1
            col = 0
        #Stops filling when rows are filled
        if row >= self.row_length:
            return True
        #Skips already filled cells
        if self.board[row][col] != 0:
            return self.fill_remaining(row, col + 1)

        # enters numbers 1 - 9
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        # Fills the whole board
        self.fill_diagonal()
        self.fill_remaining()

    def remove_cells(self):
        #Randomize the cell boxes positions on the board
        positions = [(row, col) for row in range(self.row_length) for col in range(self.row_length)]
        random.shuffle(positions)
        # Remove numbers in random spots to make the puzzle
        count = self.removed_cells
        for row, col in positions:
            if count == 0:
                break
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                count -= 1
