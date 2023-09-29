import chess
import pygame
import os
from math import inf
import copy

'''
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
'''
# Restart tree structure - keep copies of board at every node, generate tree recurssive from head node

highlight_flag = [False, 0, 0]
files = ["a", "b", "c", "d", "e", "f", "g", "h"]
to_move = "w"
starting_depth = 4
def prep_image(image_filetype:str, scalar_tuple:tuple):
    return pygame.transform.scale(pygame.image.load(os.path.join('assets', image_filetype)), (scalar_tuple))
images = {
    # Squares
    "bs": prep_image("black_square.png", (100, 100)),
    "ws": prep_image("white_square.png", (100, 100)),
    "hs": prep_image("highlight.png", (100, 100)),
    # Black Pieces
    "r": prep_image("black_rook.png", (80, 80)),
    "n": prep_image("black_knight.png", (80, 80)),
    "b": prep_image("black_bishop.png", (80, 80)),
    "q": prep_image("black_queen.png", (80, 80)),
    "k": prep_image("black_king.png", (80, 80)),
    "p": prep_image("black_pawn.png", (80, 80)),
    # White Pieces
    "R": prep_image("white_rook.png", (80, 80)),
    "N": prep_image("white_knight.png", (80, 80)),
    "B": prep_image("white_bishop.png", (80, 80)),
    "Q": prep_image("white_queen.png", (80, 80)),
    "K": prep_image("white_king.png", (80, 80)),
    "P": prep_image("white_pawn.png", (80, 80)),
}
board_tables = { # values for board evaluation
    "r": [
        [0.01, 0, 0, 0, 0, 0, 0, 0.01],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "n": [
        [0, 0.01, 0, 0, 0, 0, 0.01, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.03, 0, 0, 0.03, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "b": [
        [0, 0, 0.01, 0, 0, 0.01, 0, 0],
        [0, 0.03, 0, 0, 0, 0, 0.03, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "q": [
        [0, 0, 0, 0.01, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "k": [
        [0, 0, 0, 0, 0.01, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ],
    "p": [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0.001, 0.001, 0.001, 0.003, 0.003, 0.001, 0.001, 0.001],
        [0.002, 0.002, 0.002, 0.005, 0.005, 0.002, 0.002, 0.002],
        [0.004, 0.004, 0.004, 0.008, 0.008, 0.004, 0.004, 0.004],
    ],
}
piece_values = {
    "q": 9,
    "r": 5,
    "n": 3,
    "b": 3,
    "k": 0,
    "p": 1,
}


def draw_board_with_pieces(window:pygame.surface.Surface, board:chess.Board):
    for rank in range(8):
        for file in range(8):
            window.blit(images["bs"] if (rank + file) % 2 == 0 else images["ws"], (file * 100, 700 - (rank * 100)))
            piece_data = board.piece_at(chess.square(file, rank))
            if piece_data is not None:
                window.blit(images[str(piece_data)], ((file * 100) + 10, (700 - (rank * 100) + 10)))
            
def window_update(window:pygame.surface.Surface, board:chess.Board):
    global highlight_flag
    draw_board_with_pieces(window, board)
    highlighter(window, highlight_flag)
    pygame.display.update()

def highlight_updater(window:pygame.surface.Surface, board:chess.Board):
    global highlight_flag
    global to_move
    loc = pygame.mouse.get_pos()
    info = str(board.piece_at(chess.square(loc[0] // 100, 7 - loc[1] // 100)))
    color = "b" if info.islower() else "w"
    if info != "None" and to_move == color:
        highlight_flag = [True, loc[0] // 100, loc[1] // 100]
    else:
        gui_piece_move(board, loc)

def convert_loc_chess_notation(pos):
    global files
    x, y = pos
    return str(files[x]) + str(8 - y)

def highlighter(window:pygame.surface.Surface, highlight_flag):
    if highlight_flag[0] == True:
        window.blit(images["hs"], (highlight_flag[1] * 100, highlight_flag[2] * 100))

def gui_piece_move(board:chess.Board, loc:tuple):
    global highlight_flag
    global to_move
    first, second = convert_loc_chess_notation((highlight_flag[1], highlight_flag[2])), convert_loc_chess_notation((loc[0] // 100, loc[1] // 100))
    try:
        board.push_uci(first + second)
        if to_move == "w": to_move = "b"
        else: to_move = "w"
        highlight_flag[0] = False
        NegaMaxHandler(board)
    except Exception as e:
        try:
            board.push_uci(first + second + "q")
        except Exception as e:
            pass

def board_eval(board:chess.Board, color):
    eval = 0
    for rank in range(8):
        for file in range(8):
            piece_data = board.piece_at(chess.square(file, rank))
            piece_color = 1 if str(piece_data).islower() == True else 0
            if piece_data != None and piece_color == color:
                eval += get_relative_piece_value(str(piece_data).lower(), rank, file, True if str(piece_data).islower() == True else False) # invert tables to get relative piece value added to eval
    return eval

def get_relative_piece_value(piece_data:str, rank:int, file:int, inversion:bool):
    if inversion == True: # inverting piece position to fit bitboard
        rank = 7 - rank
    raw_piece_value = piece_values[piece_data] # piece plain value 
    raw_piece_value += board_tables[piece_data][rank][file] # positional modification
    return raw_piece_value

def generate_tree(board:chess.Board):
    # start tree
    main_root = TreeNode("head_node", 0)
    for move in board.generate_legal_moves():
        # generate node and put it in the data_location
        board.push_uci(str(move))
        root = TreeNode(str(move), board_eval(board, 1))
        main_root.add_child(root)
        for response in board.generate_legal_moves():
            board.push_uci(str(response))
            depth1 = TreeNode(str(response), board_eval(board, 0))
            root.add_child(depth1)
            for deeper in board.generate_legal_moves():
                board.push_uci(str(deeper))
                depth2 = TreeNode(str(deeper), board_eval(board, 1))
                depth1.add_child(depth2)
                board.pop()
            board.pop()
        board.pop()
    return main_root

def NegaMaxHandler(board:chess.Board, to_move:int):
    main_node = generate_tree(board)
    for node in main_node.children:
        for child_node in node.children:
            child_node.min_max_children(True if to_move == 0 else False)
        node.min_max_children(False if to_move == 0 else True)
    main_node.min_max_children(True if to_move == 0 else False)
    comp_move = str(main_node.pass_up_move())
    print(comp_move)

class TreeNode():
    def __init__(self, move, eval):
        self.move = move
        self.eval = eval
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def print_tree(self, depth):
        print("-" * depth + f"{self.move}")
        for child in self.children:
            child.print_tree(depth + 1)
        
    def min_max_children(self, min_or_max:bool): # this also prunes all the children so I can call it at every node?
        if min_or_max == True:
            max_val = -inf
            for child in self.children:
                if child.eval >= max_val:
                    max_val = child.eval
            self.eval = max_val
        else:
            min_val = inf
            for child in self.children:
                if child.eval <= min_val:
                    min_val = child.eval
            self.eval = min_val
             
    def pass_up_move(self):
        for node in self.children:
            if node.eval >= self.eval:
                self.eval = node.eval
                self.move = node.move
        return self.move
    


def main():
    pygame.init()
    window = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess Bot 2.0 Minimax/Negamax/Kalmax")
    board = chess.Board()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                highlight_updater(window, board)
                NegaMaxHandler(board, 0 if to_move == "b" else 1)
        window_update(window, board)

if __name__ == "__main__":
    main()