import pygame
from board import Board


def main():
    #####INITIALIZE PYGAME######
    pygame.init()
    width = 700
    height = 700
    screen = pygame.display.set_mode((width, height))
    over = False
    #####SET ICON AND TITLE#####
    ###Set The Title
    pygame.display.set_caption("Connect4")
    ###Load the image of the icon
    icon = pygame.image.load('src/connect-four.png')
    ### Set the Icon
    pygame.display.set_icon(icon)
    ###### BACKGROUND ##########
    ### Load the image of the background
    background = pygame.image.load('src/board.png')
    background = pygame.transform.scale(background, (800,600))
    ### Load the image of the players
    BLACK = (0,0,0)
    RED = (255,0,0)
    SQUARESIZE = 100
    RADIUS = int(SQUARESIZE/2 - 5)
    columns = 7
    rows = 6
    col_width = width/columns
    turn = 0
    ### INITIALIZE THE BOARD ###
    board = Board()
    while over is not True:

        screen.fill((255,255,255))

        for event in pygame.event.get():
            #### QUIT CONDITION #####
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    x_pressed, y_pressed = pygame.mouse.get_pos()
                    col_pos = x_pressed//col_width
                    if turn == 0:
                        board.insert_into_board(int(col_pos), 'Player1')
                    else:
                        board.insert_into_board(int(col_pos), 'Player2')
                    turn += 1

        board.draw(screen)
        over = board.game_over()

        x,y = pygame.mouse.get_pos()
        if x> 0  and x< width:
            if turn == 0:
                pygame.draw.circle(screen, RED, (x, int(SQUARESIZE/2)), RADIUS)
            else: 
                pygame.draw.circle(screen, BLACK, (x, int(SQUARESIZE/2)), RADIUS)

        turn = turn%2
        pygame.display.update()
    
    winner = board.winner
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    text_surface = my_font.render(f'The winner is PLAYER {winner} !', False, (255, 255, 255))
    
    while over:

        screen.fill((0,0,0))
        screen.blit(text_surface, (100,350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = False

        pygame.display.update()

    pygame.quit()


def terminal_main() -> None:
    board = Board()
    player = 0
    over = False
    while over is not True:
        board.display()
        print(over)
        if player == 0:
            col = int(input("Where do player1 wants to place his peace? "))
            board.insert_into_board(col, 'Player1')
        else:
            col = int(input("Where do player2 wants to place his peace"))
            board.insert_into_board(col, 'Player2')
        player += 1
        player = player%2
        over = board.game_over()
    winner = board.winner
    board.display()
    print("The winner is: ", winner)

if __name__ == "__main__":
    main()