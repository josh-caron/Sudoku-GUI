import pygame
import constants

class Cell:
    def __init__(self, value, row, col, screen):

        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.temporary_value = None

    def set_cell_value(self, value):
        """
        Sets the final chosen value for the cell.
        """
        self.value = value

    def set_temporary_value(self, value):
        """
        Sets a temporary value for display before final input.
        """
        self.temporary_value = value

    def draw(self):
        """
        Draws the cell on the screen, including its background, border,
        and any displayed value or temporary value.
        """
        cell_size = 60
        cell_position = (self.col * cell_size, self.row * cell_size)
        rectangle = pygame.Rect(*cell_position, cell_size, cell_size)

        # Draw cell background
        pygame.draw.rect(self.screen, constants.WHITE, rectangle)

        # Draw cell border (red if selected, black otherwise)
        border_color = constants.RED if self.selected else constants.BLACK
        pygame.draw.rect(self.screen, border_color, rectangle, 3 if self.selected else 1)

        # Render and draw the value or temporary value
        font = pygame.font.Font(None, constants.MEDIUM_FONT)
        if self.value != 0:
            # Draw the finalized value in black
            text = font.render(str(self.value), True, constants.BLACK)
            text_position = (cell_position[0] + 20, cell_position[1] + 10)
            self.screen.blit(text, text_position)
        elif self.temporary_value is not None:
            # Draw the temporary value in gray
            text = font.render(str(self.temporary_value), True, constants.GRAY)
            text_position = (cell_position[0] + 5, cell_position[1] + 5)
            self.screen.blit(text, text_position)
