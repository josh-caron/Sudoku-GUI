import pygame
import sys
from constants import *
from board import Board
#Sets up the Pygame modules for us to use
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sudoku")


def game_start_screen(screen):
    # Show the game start screen
    font_large = pygame.font.Font(None, LARGE_FONT)
    font_medium = pygame.font.Font(None, MEDIUM_FONT)


    running = True
    while running:
        screen.fill(WHITE) #Fills background with White

        # Draw text for title and sets fonts
        title_text = font_large.render("Welcome to Sudoku", True, BLACK)
        screen.blit(title_text, (screen.get_width() // 2 - title_text.get_width() // 2, 100))

        select_text = font_medium.render("Select Game Mode:", True, BLACK)
        screen.blit(select_text, (screen.get_width() // 2 - select_text.get_width() // 2, 200))

        # Handles button dimensions and positions
        button_width, button_height = 120, 50
        spacing = 20
        total_width = 3 * button_width + 2 * spacing
        start_x = (screen.get_width() - total_width) // 2
        easy_button = pygame.Rect(start_x, 300, button_width, button_height)
        medium_button = pygame.Rect(start_x + button_width + spacing, 300, button_width, button_height)
        hard_button = pygame.Rect(start_x + 2 * (button_width + spacing), 300, button_width, button_height)
        
        #Draws buttons with orange colors!
        pygame.draw.rect(screen, ORANGE, easy_button)
        pygame.draw.rect(screen, ORANGE, medium_button)
        pygame.draw.rect(screen, ORANGE, hard_button)

        # Draws the text for buttons
        easy_text = font_medium.render("EASY", True, WHITE)
        medium_text = font_medium.render("MEDIUM", True, WHITE)
        hard_text = font_medium.render("HARD", True, WHITE)

        screen.blit(easy_text, (easy_button.x + button_width // 2 - easy_text.get_width() // 2,
                                easy_button.y + button_height // 2 - easy_text.get_height() // 2))
        screen.blit(medium_text, (medium_button.x + button_width // 2 - medium_text.get_width() // 2,
                                  medium_button.y + button_height // 2 - medium_text.get_height() // 2))
        screen.blit(hard_text, (hard_button.x + button_width // 2 - hard_text.get_width() // 2,
                                hard_button.y + button_height // 2 - hard_text.get_height() // 2))

# Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if easy_button.collidepoint(pos):
                    return 30 #returns 30 so difficulty is easy
                elif medium_button.collidepoint(pos):
                    return 40 #returns 40 so difficulty is medium
                elif hard_button.collidepoint(pos):
                    return 50 #returns 50 so difficulty is hard

        pygame.display.flip() #updates screen


def draw_game_buttons(screen):
# Draw reset, restart, and exit buttons
    font = pygame.font.Font(None, SMALL_FONT) #fonts for the buttons
    button_width, button_height = 100, 40 #sizes of buttons
    spacing = 20 #handles spacing between buttons
    total_width = 3 * button_width + 2 * spacing #total width which the buttons occupy
    start_x = (screen.get_width() - total_width) // 2 #centering buttons

    #Creates button rectangles using dimensions found from above
    reset_button = pygame.Rect(start_x, 550, button_width, button_height)
    restart_button = pygame.Rect(start_x + button_width + spacing, 550, button_width, button_height)
    exit_button = pygame.Rect(start_x + 2 * (button_width + spacing), 550, button_width, button_height)
    #Draw buttons with yet again an orange color as we did on line 38 to 40
    pygame.draw.rect(screen, ORANGE, reset_button)
    pygame.draw.rect(screen, ORANGE, restart_button)
    pygame.draw.rect(screen, ORANGE, exit_button)
    #Draws text again for the options for the user to read
    reset_text = font.render("RESET", True, WHITE)
    restart_text = font.render("RESTART", True, WHITE)
    exit_text = font.render("EXIT", True, WHITE)
    #Centers text on each button
    screen.blit(reset_text, (reset_button.x + button_width // 2 - reset_text.get_width() // 2,
                             reset_button.y + button_height // 2 - reset_text.get_height() // 2))
    screen.blit(restart_text, (restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                               restart_button.y + button_height // 2 - restart_text.get_height() // 2))
    screen.blit(exit_text, (exit_button.x + button_width // 2 - exit_text.get_width() // 2,
                            exit_button.y + button_height // 2 - exit_text.get_height() // 2))

    return reset_button, restart_button, exit_button


def game_won_screen(screen):
# Show the game won screen
# Also sets font sizes
    font_large = pygame.font.Font(None, LARGE_FONT)
    font_medium = pygame.font.Font(None, MEDIUM_FONT)

    running = True
    while running:
        screen.fill((255, 255, 255)) #fills background with White

        # Draw winning message!
        win_text = font_large.render("Game Won!", True, GREEN)
        screen.blit(win_text, (screen.get_width() // 2 - win_text.get_width() // 2, 200))

        # Draw restart button!
        button_width, button_height = 150, 50
        restart_button = pygame.Rect(
            screen.get_width() // 2 - button_width // 2, 350, button_width, button_height
        )
        pygame.draw.rect(screen, ORANGE, restart_button)

        restart_text = font_medium.render("RESTART", True, WHITE)
        screen.blit(
            restart_text,
            (
                restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                restart_button.y + button_height // 2 - restart_text.get_height() // 2,
            ),
        )
        #Handles event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(pos):
                    return "restart"

        pygame.display.flip()


def game_over_screen(screen):
    # Show the game over screen
    # Again sets font sizes
    font_large = pygame.font.Font(None, LARGE_FONT)
    font_medium = pygame.font.Font(None, MEDIUM_FONT)

    running = True
    while running:
        screen.fill(WHITE)

        # Draw game over text!
        lose_text = font_large.render("Game Over :( You lose. ", True, RED)
        screen.blit(lose_text, (screen.get_width() // 2 - lose_text.get_width() // 2, 200))

        # Draw restart button!
        button_width, button_height = 150, 50
        restart_button = pygame.Rect(
            screen.get_width() // 2 - button_width // 2, 350, button_width, button_height
        )
        pygame.draw.rect(screen, ORANGE, restart_button)

        restart_text = font_medium.render("RESTART", True, WHITE)
        screen.blit(
            restart_text,
            (
                restart_button.x + button_width // 2 - restart_text.get_width() // 2,
                restart_button.y + button_height // 2 - restart_text.get_height() // 2,
            ),
        )
        #Handles event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if restart_button.collidepoint(pos):
                    return "restart"

        pygame.display.flip()


def main():
    # Display start screen and gets selected difficulty
    difficulty = game_start_screen(screen)
    board = Board(540, 540, screen, difficulty)
    #Game Loop
    while True:
        screen.fill(WHITE) #Fills background with White
        board.draw() #Draws Board
        #Draws buttons for user controls
        reset_button, restart_button, exit_button = draw_game_buttons(screen)
        #Handles event loops
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #Handles resetting, restarting, and exiting the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if reset_button.collidepoint(pos):
                    board.reset_to_original()
                elif restart_button.collidepoint(pos):
                    return main()
                elif exit_button.collidepoint(pos):
                    pygame.quit()
                    sys.exit()
                else: #Calculates row and column for click of cell by user
                    row, col = pos[1] // 60, pos[0] // 60
                    if row < 9 and col < 9:
                        board.select(row, col)

            #Add the ability to delete inputs
            elif event.type == pygame.KEYDOWN:
                if pygame.K_1 <= event.key <= pygame.K_9:
                    value = event.key - pygame.K_0
                    board.sketch(value)
                elif event.key == pygame.K_RETURN:
                    if board.selected_cell and board.selected_cell.temporary_value:
                        board.place_number(board.selected_cell.temporary_value)
                elif event.key == pygame.K_BACKSPACE:
                    board.delete_value()
        #Checks if board is full 
        if board.is_full():
            if board.check_board():
                if game_won_screen(screen) == "restart":
                    return main()
            else:
                if game_over_screen(screen) == "restart":
                    return main()

        pygame.display.flip()


if __name__ == "__main__":
    main()
