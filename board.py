from itertools import groupby
import numpy as np
import pygame


class Board:
    def __init__(self) -> None:
        self.board = [[0 for i in range(7)] for j in range(6)]
        self.winner = 0

    def insert_into_board(self, column, player):
        for i in range(len(self.board)):
            if player == 'Player1' and self.board[len(self.board)-1-i][column] == 0:
                self.board[len(self.board)-1-i][column] = 1
                break
            if player == 'Player2' and self.board[len(self.board)-1-i][column] == 0:
                self.board[len(self.board)-1-i][column] = 2
                break

    def __iter__(self) -> None:
        for _ in self.board:
            yield _

    def display(self) -> None:
        for _ in self.board:
            print(_)
        print([0,1,2,3,4,5,6])

    def reset(self) -> None:
        self.board = [[0 for i in range(7)] for j in range(6)]

    def _check_list(self, lst):
        sum = 0
        value = 0
        for _, g in groupby(lst):
            for _ in g:
                if _ > 0:
                    sum += 1
                    value = _
            if sum >= 4:
                return True, value
            else:
                sum = 0
                value = _
        return False

    def game_over(self) -> bool:
        game_over = False
        if self.check_row() == (True, 1) or self.check_column() == (True, 1) or self.check_diagonal() == (True, 1):
            game_over = True
            self.winner = 1
        if self.check_row() == (True, 2) or self.check_column() == (True, 2) or self.check_diagonal() == (True, 2):
            game_over = True
            self.winner = 2
        return game_over

    def check_row(self):
        for i in self.board:
            if self._check_list(i) == (True, 1):
                return True, 1
            elif self._check_list(i) == (True, 2):
                return True, 2
        return False, 0
                
    def check_column(self):
        col = []
        for i in range(7):
            for j in range(6):
                col.append(self.board[j][i])
            if self._check_list(col) == (True, 1):
                return True, 1
            elif self._check_list(col) == (True, 2):
                return True, 2
            else:
                col = []
        return False, 0

    def check_diagonal(self):
        for i in range(-2,4):
            if self._check_list(np.diag(self.board, k=i)) == (True, 1):
                return True, 1
            elif self._check_list(np.diag(self.board, k=i)) == (True, 2):
                return True, 2
            if self._check_list(np.diag(np.fliplr(self.board), k=i)) == (True, 1):
                return True, 1
            elif self._check_list(np.diag(np.fliplr(self.board), k=i)) == (True, 2):
                return True, 2
        return False, 0

    def draw(self, surface):
        COLUMN_COUNT = 7
        SQUARESIZE = 100
        RADIUS = int(SQUARESIZE/2 - 5)
        ROW_COUNT = 6
        BLUE = (0,0,255)
        WHITE = (255,255,255)
        RED = (255,0,0)
        YELLOW = (255,255,0)
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):
                pygame.draw.rect(surface, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
                pygame.draw.circle(surface, WHITE, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT):		
                if self.board[r][c] == 1:
                    pygame.draw.circle(surface, RED, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE/2) + SQUARESIZE), RADIUS)
                elif self.board[r][c] == 2: 
                    pygame.draw.circle(surface, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE/2) + SQUARESIZE), RADIUS)

