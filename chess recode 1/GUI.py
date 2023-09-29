import chess
import pygame
import os

class gameDisplay():
    def __init__(self, board:chess.Board):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("Chess Bot 2.0 - Minimax/Negamax")
        self.images = {
            # squares
            "bs": self.prep_image("black_square.png", (100, 100)),
            "ws": self.prep_image("white_square.png", (100, 100)),
            "hs": self.prep_image("highlight.png", (100, 100)),
            # black pieces
            "r": self.prep_image("black_rook.png", (80, 80)),
            "n": self.prep_image("black_knight.png", (80, 80)),
            "b": self.prep_image("black_bishop.png", (80, 80)),
            "q": self.prep_image("black_queen.png", (80, 80)),
            "k": self.prep_image("black_king.png", (80, 80)),
            "p": self.prep_image("black_pawn.png", (80, 80)),
            # white pieces
            "R": self.prep_image("white_rook.png", (80, 80)),
            "N": self.prep_image("white_knight.png", (80, 80)),
            "B": self.prep_image("white_bishop.png", (80, 80)),
            "Q": self.prep_image("white_queen.png", (80, 80)),
            "K": self.prep_image("white_king.png", (80, 80)),
            "P": self.prep_image("white_pawn.png", (80, 80))
        }
        self.highlight = [False, 0, 0]
        self.window.blit(self.images["ws"], (100, 100))
    
    def prep_image(self, image_name, scale):
        return pygame.transform.scale(pygame.image.load(os.path.join("assets", f"{image_name}")), (scale))
    
    def update_window(self, board:chess.Board):
        self.draw_board(board)

        pygame.display.update()
    
    def draw_board(self, board:chess.Board):
        for rank in range(8):
            for file in range(8):
                self.window.blit(self.images["bs"] if (rank + file) % 2 == 1 else self.images["ws"], (file * 100, rank * 100))
                if board.piece_at(chess.square(file, rank)) != None:
                    self.window.blit(self.images[str(board.piece_at(chess.square(file, rank)))], ((file * 100) + 10, 700 - (rank * 100) + 10))
