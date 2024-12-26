import pygame
import constants
from cell import Cell
from sudoku_generator import SudokuGenerator


class Board:
    def __init__(self, width, height, screen, difficulty):
        #Sets the boards Size, screen color, and difficulty settings.

        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # Generates the board for sudoku
        self.sudoku_generator = SudokuGenerator(9, difficulty)
        #Fills the boards cells with numbers
        self.sudoku_generator.fill_values()
        #Removes numbers from the board corresponding to the level
        self.sudoku_generator.remove_cells()

        # Makes the cells for the board
        self.board = self.sudoku_generator.get_board()
        self.cells = [[Cell(self.board[row][col], row, col, screen) for col in range(9)] for row in range(9)]

        #Checks the cell clicked on corresponding to how the board was originally
        self.selected_cell = None
        self.original_board = [[cell.value for cell in row] for row in self.cells]

    def draw(self):
        # Draw all cells on the board
        for row in range(9):
            for col in range(9):
                self.cells[row][col].draw()

        # Draw grid lines for the board
        for i in range(10):
            #Makes the 3x3 distinct boxes have thicker lines
            thickness = 5 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, constants.BLACK, (0, i * 60), (540, i * 60), thickness)  # Horizontal
            pygame.draw.line(self.screen, constants.BLACK, (i * 60, 0), (i * 60, 540), thickness)  # Vertical

    def select(self, row, col):
        # Highlight a cell when the user clicks on the box
        if self.selected_cell:
            self.selected_cell.selected = False
        self.selected_cell = self.cells[row][col]
        self.selected_cell.selected = True

    def sketch(self, value):
        # Add a temporary value to a cell before the user enters the number
        if self.selected_cell and self.selected_cell.value == 0:
            self.selected_cell.set_temporary_value(value)

    def place_number(self, value):
        # Set a value in a cell after the user entered the sketched cell
        if self.selected_cell and self.selected_cell.value == 0:
            #Puts the final value into the cell
            self.selected_cell.set_cell_value(value)
            #Removes the temporary cell one the final is entered
            self.selected_cell.temporary_value = None
            #Updates the board after the cell has been entered
            self.update_board()

    def reset_to_original(self):
        # Resets the board to the starting board
        for row in range(9):
            for col in range(9):
                #Restores the values to the original state
                self.cells[row][col].value = self.original_board[row][col]
                #Removes the temporary numbers from the board
                self.cells[row][col].temporary_value = None

    def is_full(self):
        # Check if the board is completely filled
        return all(cell.value != 0 for row in self.cells for cell in row)

    def delete_value(self):
        # Delete the value in the selected cell if it was not part of the original board
        if self.selected_cell and self.original_board[self.selected_cell.row][self.selected_cell.col] == 0:
            self.selected_cell.set_cell_value(0)
            self.selected_cell.temporary_value = None

    def check_board(self):
        # Check if the board is correct solution
        for row in range(9):  # Check rows if they add to 9
            if len(set(cell.value for cell in self.cells[row])) != 9:
                return False

        for col in range(9):  # Checks columns
            if len(set(self.cells[row][col].value for row in range(9))) != 9:
                return False

        for box_row in range(0, 9, 3):  # Check 3x3 boxes
            for box_col in range(0, 9, 3):
                box = [self.cells[row][col].value for row in range(box_row, box_row + 3) for col in
                       range(box_col, box_col + 3)]
                if len(set(box)) != 9:
                    return False

        return True

    def update_board(self):
        # Update the board with cell values to its most recent enters
        self.board = [[cell.value for cell in row] for row in self.cells]


