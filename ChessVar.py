# Author: Colleen S. H. Velasco
# GitHub username: colleensvelasco
# Date: November 27, 2023
# Description: A program that is a chess game variant where the chess pieces move the same as they do in real chess,
#              but without castling, en passant, and pawn promotion. The first player side to capture all the
#              opponent's pieces of one chess piece type wins.

import string

class ChessVar:
    """Represents a variant of chess consisting of a game board, white side, black side, current turn of
    the game, and round number. To win the game, one side must capture all of an opponent's pieces of one type."""

    def __init__(self):
        """Creates a ChessVar game with a board, black and white sides, a current turn (side),  round number,
        row to list in board converter (dictionary), column to order num in list converter (dictionary).
        Initializes board as empty list and white_side as an object of WhiteSide class and black_side as an object
        of BlackSide class. Current turn is initialized to white. Round number initialized to 1."""
        self._board = self.create_game_board()
        self._white_side = WhiteSide()
        self._black_side = BlackSide()
        self._current_turn = "white"
        self._round_number = 1
        self._row_to_list = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7 }  # Row to list converter
                                                                                               # Keys=Row, values=list
        self._col_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}    # Column to num converter

    def create_game_board(self):
        """Creates starting game board 8x8 (rows 1-8) and (columns a-h) consisting of 8 lists (each with 8 elements)
        within the board (an empty list initially). If a square is empty, it is occupied with a "-" in the list.
        For an occupied square, it contains {"location": [color side occupying, chess piece]}.
        For example: {"c2":["white", "pawn"]}"""
        board_whole = list()
        ind = 8
        for each_row in range(8):
            row = []
            if each_row == 0 or each_row == 7:
                # If this is the first or last row
                if each_row == 0:
                    # First row is black side's back row
                    color = "black"
                else:
                    # Last row is white side's back row
                    color = "white"
                for place in range(8):
                    location = string.ascii_lowercase[place] + str(each_row + ind)
                    if place == 0 or place == 7:
                        # Places rooks
                        chess_piece = "rook"
                    if place == 1 or place == 6:
                        # Places knights
                        chess_piece = "knight"
                    if place == 2 or place == 5:
                        # Places bishops
                        chess_piece = "bishop"
                    if place == 3:
                        # Place queen
                        chess_piece = "queen"
                    if place == 4:
                        # Place king
                        chess_piece = "king"

                    row.append(f"{location}: {color} {chess_piece}")
            elif each_row == 1 or each_row == 6:
                # If pawn row
                chess_piece = "pawn"
                if each_row == 1:
                    # This row is black pawns
                    color = "black"
                else:
                    # This row is white pawns
                    color = "white"
                for place in range(8):
                    location = string.ascii_lowercase[place] + str(each_row + ind)
                    row.append(f"{location}: {color} {chess_piece}")
            else:
                # Empty squares
                for place in range(8):
                    empty = "-"
                    location = string.ascii_lowercase[place] + str(each_row + ind)
                    row.append(f"{location}: {empty} {empty}")
            ind -= 2
            board_whole.append(row)
        return board_whole

            # Keys=Col, values=num

    def display_board(self):
        """Prints current board. Iterates through board and prints what each square contains."""
        for row in self._board:
            print([square for square in row])
            print()

    def get_game_state(self):
        """Checks for the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON.' A
        side wins when one has captured all of an opponent's pieces of one type. Checks white side and black side
        (WhiteSide and BlackSide objects) to see if any of the collected chess pieces in their score contains
        all of that kind."""
        # Returns dictionary score for each side
        white_score = self._white_side.get_score()
        black_score = self._black_side.get_score()
        if (white_score["pawn"] == 8 or white_score["rook"] == 2 or white_score["knight"] == 2 or
            white_score["bishop"] == 2 or white_score["queen"] == 1 or white_score["king"] == 1):
            return "WHITE_WON"
        elif (black_score["pawn"] == 8 or black_score["rook"] == 2 or black_score["knight"] == 2 or
            black_score["bishop"] == 2 or black_score["queen"] == 1 or black_score["king"] == 1):
            return "BLACK_WON"
        # Otherwise, game is unfinished:
        return "UNFINISHED"


    def turn_changer(self):
        """Checks whose current_turn it is (black or white) and switches current_turn to other side. Every time black
        makes a move we finish a round, so we update round_number when current_turn changes from 'black' to 'white.'"""
        if self._current_turn == "black":
            # If it was just black's turn, make it white's turn and go on to next round
            self._current_turn = "white"
            self._round_number += 1
        else:
            # If it was just white's turn, make it black's turn
            self._current_turn = "black"

    def get_current_turn(self):
        """Returns current_turn (current player)."""
        return self._current_turn

    def set_square(self, sq_location, side_color, chess_piece):
        """Takes square location and the side color and chess piece that will occupy the given square and updates it.
        Side color and chess piece can be None if square is now empty."""
        row = sq_location[1]                                            # Gets number of row
        col = sq_location[0]                                            # Gets letter column
        row_num = int(self._row_to_list[row])                               # Converts row to list in board
        col_order = self._col_to_num[col]                           # Converts column to order num in list of board

        if chess_piece == "-":
            # If square is now empty
            self._board[row_num][col_order] = f"{sq_location}: {side_color} {chess_piece}"
        else:
            # If new chess piece occupies square, update
            self._board[row_num][col_order] = f"{sq_location}: {side_color} {chess_piece}"

    def get_square(self, sq_location):
        """Takes square location string and returns what's contained in that square. If square has "-" as value to
        location key square is empty and returns None."""
        row = sq_location[1]                                            # Gets number of row
        col = sq_location[0]                                            # Gets letter column
        row_num = int(self._row_to_list[row])                               # Converts row to list in board
        col_order = self._col_to_num[col]                           # Converts column to order num in list of board
        sq = self._board[row_num][col_order]                       # Contents of sq

        return sq              # "sq_location: side color chess piece" and "sq_location: - -" if empty

    def is_move_legal(self, original_sq, destination_sq):
        """Takes the square moved from (original_sq) (i.e. "b3")and square moved to (destination_sq). Checks the chess piece
        in the original_sq and makes sure the change in location is legal for that piece type. If not legal or other
        pieces in path, returns False. Otherwise, returns True. To check what's in square, calls get_square."""

        in_original_sq = self.get_square(original_sq)
        if "-" in in_original_sq or in_original_sq[4:9] != self._current_turn:
            # If original square is empty or if has opponent piece
            return False

        in_dest_sq = self.get_square(destination_sq)
        if in_dest_sq[4:9] == self._current_turn:
            # If destination square is occupied and has current turn's piece
            return False

        # ALREADY CHECKED FOR INVALIDITY IN ORIGINAL AND DESTINATION SQUARES,
        # CHECK ON CHESS PIECE VALIDITY

        if in_original_sq[1] == "pawn":
            pawn_move = PawnMove(original_sq, destination_sq)
            return pawn_move.is_move_valid(self._round_number, self._board)

        elif in_original_sq[1] == "rook":
            rook_move = RookMove(original_sq, destination_sq)
            return rook_move.is_move_valid(self._board)

        elif in_original_sq[1] == "knight":
            knight_move = KnightMove(original_sq, destination_sq)
            return knight_move.is_move_valid()

        elif in_original_sq[1] == "bishop":
            bishop_move = BishopMove(original_sq, destination_sq)
            return bishop_move.is_move_valid(self._board)

        elif in_original_sq[1] == "queen":
            queen_move = QueenMove(original_sq, destination_sq)
            return queen_move.is_move_valid(self._board)

        elif in_original_sq[1] == "king":
            king_move = KingMove(original_sq, destination_sq)
            return king_move.is_move_valid()


    def make_move(self, original_sq, destination_sq):
        """Takes strings representing square moved from and square moved to. If square moved from has
        opponent's piece, illegal move attempted (calls is_move_legal to check), or game is over
        (calling get_game_state), returns False. Otherwise, makes indicated move and removes captured piece (if any)
        (calling set_square to do so), updates score (if needed), update whose turn (turn_changer), and returns True."""
        print(f"from_square is {original_sq} and to_square is {destination_sq}")

        # Checks if original_sq has opponent or empty, if destination_sq has current player's piece, or if move is
        # illegal -> if so, return FALSE
        if self.is_move_legal(original_sq, destination_sq) is False:
            return False

        # Check is game over - get_game_state -> if so, False
        elif self.get_game_state() == "WHITE_WON" or self.get_game_state() == "BLACK_WON":
            return False

        # Otherwise:
        # Make move - empty original_sq and destination_sq (if has opponent, update score & move - if not, just move)
        # Update turn
        else:
            in_orig_square = self.get_square(original_sq)
            in_dest_square = self.get_square(destination_sq)

            # If destination sq is occupied and has opponent, update score of current player
            if "-" not in in_dest_square and in_dest_square[4:9] != self._current_turn:
                if self._current_turn == "white":
                    self._white_side.set_score(in_dest_square[10:])
                elif self._current_turn == "black":
                    self._black_side.set_score(in_dest_square[10:])

            # Still make move regardless
            self.set_square(original_sq, "-", "-")                                  # empty original_sq
            self.set_square(destination_sq, self._current_turn, in_orig_square[10:]) # update destination_sq with current
                                                                                    # player and its chess piece
            # Update turn
            self.turn_changer()

            return True

class BlackSide:
    """Represents the black side of the chess variant game."""

    def __init__(self):
        """Creates the BlackSide of the chess variant game with a score (dictionary where keys= chess pieces and
        values= number of opponent pieces collected (initialized to 0)."""
        self._score = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    def set_score(self, piece_collected):
        """Takes name of chess piece collected (string) and updates BlackSide's score."""
        self._score[piece_collected] += 1               # Increments chess piece collected score by 1

    def get_score(self):
        """Returns BlackSide score."""
        return self._score


class WhiteSide:
    """Represents the white side of the chess variant game."""

    def __init__(self):
        """Creates the WhiteSide of the chess variant game with a score (dictionary where keys= chess pieces and
        values= number of opponent pieces collected (initialized to 0)."""
        self._score = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    def set_score(self, piece_collected):
        """Takes name of chess piece collected (string) and updates WhiteSide's score."""
        self._score[piece_collected] += 1               # Increments chess piece collected score by 1

    def get_score(self):
        """Returns WhiteSide score."""
        return self._score

class ChessPieceMove:
    """Represents a ChessPieceMove with an original square and destination square."""
    def __init__(self, original_sq, destination_sq):
        """Creates a ChessPieceMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        self._original_sq = original_sq    # COL LETTER, ROW NUMBER "b7"
        self._destination_sq = destination_sq
        self._row_to_list = {"8": 0, "7": 1, "6": 2, "5": 3, "4": 4, "3": 5, "2": 6, "1": 7}  # Row to list converter
        self._col_to_num = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}  # Column to num converter



class PawnMove(ChessPieceMove):
    """Represents a PawnMove that inherits from ChessPieceMove."""
    def __init__(self, original_sq, destination_sq):
        """Creates a PawnMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self, round_number, board_game):
        """Checks if proposed pawn move is valid. Pawns can move forward 1 and if it's the first move, can move
        forward 2."""
        row_orig = self._row_to_list[self._original_sq[1]]  # gets row -> corresponding list NUM
        col_orig = self._col_to_num[self._original_sq[0]]   # gets column -> corresponding order NUM in list

        row_dest = self._row_to_list[self._destination_sq[1]]
        col_dest = self._col_to_num[self._destination_sq[0]]


        if round_number == 1:
            # Pawn can move 2 or 1 if it's the first move for that side
            if abs(row_orig-row_dest) == 2 and col_orig == col_dest:
                if row_orig > row_dest:
                    sq_bw = board_game[row_dest+1][col_orig]
                    if "-" not in sq_bw:
                        return False
                elif row_dest > row_orig:
                    sq_bw = board_game[row_orig + 1][col_orig]
                    if "-" not in sq_bw:
                        return False
                return True                                      # if nothing in the way
        # If not first move, can only move forward 1
        return abs(row_orig-row_dest) == 1 and col_orig == col_dest

class RookMove(ChessPieceMove):
    """Represents a RookMove that inherits from ChessPieceMove."""

    def __init__(self, original_sq, destination_sq):
        """Creates a RookMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self, game_board):
        """Checks if proposed rook move is valid. Rooks can move forwards, backwards, or sideways any number
        of squares, as long as no other pieces are in its way."""
        row_orig = self._row_to_list[self._original_sq[1]]  # gets row -> corresponding list NUM
        col_orig = self._col_to_num[self._original_sq[0]]  # gets column -> corresponding order NUM in list

        row_dest = self._row_to_list[self._destination_sq[1]]
        col_dest = self._col_to_num[self._destination_sq[0]]

        if row_orig == row_dest:
            # Piece is moving sideways - SAME ROW
            if col_orig > col_dest:                                          # trying to move left (from starting board)
                for each_col_num in range(col_dest + 1, col_orig):
                    sq = game_board[row_orig][each_col_num]
                    if "-" not in sq:
                        return False                                         # piece in way
            elif col_dest > col_orig:                                        # trying to move right (from starting board)
                for each_col_num in range(col_orig + 1, col_dest):
                    sq = game_board[row_orig][each_col_num]
                    if "-" not in sq_bw:
                        return False                                         # piece in way
            return True                                                      # No piece in the way

        elif col_orig == col_dest:
            # Piece is moving forwards/backwards - SAME COLUMN
            if row_dest > row_orig:                                          # trying to move down (from starting board)
                for row_num in range(row_orig+1, row_dest):
                    sq = game_board[row_num][col_orig]
                    if "-" not in sq:
                        return False
            elif row_orig > row_dest:                                        # trying to move up (from starting board)
                for row_num in range(row_dest+1, row_orig):
                    sq = game_board[row_num][col_orig]
                    if "-" not in sq:
                        return False
            return True                                                      # No piece in the way
        # If tried diagonal:
        return False

class KnightMove(ChessPieceMove):
    """Represents a KnightMove that inherits from ChessPieceMove."""
    def __init__(self, original_sq, destination_sq):
        """Creates a KnightMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self):
        """Checks if proposed knight move is valid. Knights can move in an L shape (moving 2 and moving 1 in different
        directions) and can jump over other pieces."""
        row_orig = self._row_to_list[self._original_sq[1]]  # gets row -> corresponding list NUM
        col_orig = self._col_to_num[self._original_sq[0]]  # gets column -> corresponding order NUM in list

        row_dest = self._row_to_list[self._destination_sq[1]]
        col_dest = self._col_to_num[self._destination_sq[0]]

        if abs(row_orig - row_dest) == 2 and abs(col_orig - col_dest) == 1:
            return True
        elif abs(col_orig - col_dest) == 2 and abs(row_orig - row_dest) == 1:
            return True
        # If L shape is not made:
        return False



class BishopMove(ChessPieceMove):
    """Represents a BishopMove that inherits from ChessPieceMove."""
    def __init__(self, original_sq, destination_sq):
        """Creates a BishopMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self, game_board):
        """Checks if proposed bishop move is valid."""
        row_orig = self._row_to_list[self._original_sq[1]]  # gets row -> corresponding list NUM
        col_orig = self._col_to_num[self._original_sq[0]]  # gets column -> corresponding order NUM in list

        row_dest = self._row_to_list[self._destination_sq[1]]
        col_dest = self._col_to_num[self._destination_sq[0]]

        if abs(row_orig - row_dest) == abs(col_orig - col_dest):
            # if moving diagonally, check to see if no pieces in the way
            if row_dest < row_orig:
                # If row decreasing
                row_start, row_stop = row_dest, row_orig
                if col_dest < col_orig:
                    # If row and col decreasing
                    col_start, col_stop = col_dest, col_orig
                elif col_dest > col_orig:
                    # if row decreasing, col increasing
                    col_start, col_stop = col_orig, col_dest
            elif row_dest > row_orig:
                # If row increasing
                row_start, row_stop = row_orig, row_dest
                if col_dest > col_orig:
                    # If row and col increasing
                    col_start, col_stop = col_orig, col_dest
                if col_dest < col_orig:
                    # If row increasing, col decreasing
                    col_start, col_stop = col_dest, col_orig

            while row_start < row_stop and col_start < col_stop:
                row_start += 1
                col_start += 1
                sq = game_board[row_start][col_start]
                if "-" not in sq:
                    return False
            # If diagonal and no piece found in its way, return True
            return True
        # Not moving diagonally
        else:
            return False



class QueenMove(ChessPieceMove):
    """Represents a QueenMove that inherits from ChessPieceMove."""
    def __init__(self, original_sq, destination_sq):
        """Creates a QueenMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self, game_board):
        """Checks if proposed queen move is valid. Queen can move like a rook or bishop."""
        rook_move = RookMove(self._original_sq, self._destination_sq)
        bishop_move = BishopMove(self._original_sq, self._destination_sq)

        # If its a valid rook or bishop move it's a valid queen move
        return rook_move.is_move_valid(game_board) or bishop_move.is_move_valid(game_board)


class KingMove(ChessPieceMove):
    """Represents a KingMove that inherits from ChessPieceMove."""
    def __init__(self, original_sq, destination_sq):
        """Creates a KingMove with an original_sq, destination_sq, row to list int converter, and column to order
        num in list converter."""
        super().__init__(original_sq, destination_sq)

    def is_move_valid(self):
        """Checks if proposed king move is valid. King can move 1 square in any direction."""
        row_orig = self._row_to_list[self._original_sq[1]]  # gets row -> corresponding list NUM
        col_orig = self._col_to_num[self._original_sq[0]]  # gets column -> corresponding order NUM in list

        row_dest = self._row_to_list[self._destination_sq[1]]
        col_dest = self._col_to_num[self._destination_sq[0]]

        if abs(row_orig-row_dest) == 1 and col_orig == col_dest:
            # if moved backward or forward 1
            return True
        elif abs(col_orig-col_dest) == 1 and row_orig == row_dest:
            # if moved sideways 1
            return True
        elif abs(row_orig-row_dest) == 1 and abs(col_orig-col_dest) == 1:
            # if moved diagonally 1
            return True
        # if 1 square was not moved
        return False



#   DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS

# 1. Initializing the ChessVar class: The ChessVar class has five private data members and within its init method
#    we initialize the board to be an empty list, white_side to be an object of the WhiteSide class, black_side to be
#    an object of the BlackSide class, current_turn to be "white" since the white side makes the first move in
#    chess, and round_number to be 1.
#
# 2. Keeping track of turn order: The white side always makes the first move in chess, so the ChessVar class data
#    member current_turn is initialized to 'white.' If make_move makes a correct move, we call turn_changer within that
#    method that changes current_turn to the opposing side and updates data member round_number every time we transition
#    from black to white, the completion of a round.
#
# 3. Keeping track of the current board position: Once we begin the game and the ChessVar class has been initialized,
#    we call the create_game_board method to create the starting board that's 8x8 (rows 1-8) and (columns a-h)
#    consisting of 8 lists (each with 8 elements) within the board (an empty list initially).
#    An occupied square contains {"location": [color side occupying, chess piece]}, such as {"c2":["white", "pawn"]}.
#    If a square is empty, it is occupied with a "-".
#    To check what's at current square, we can call get_square method that returns
#    {"location": [color side occupying, chess piece]} if occupied, and returns None if empty.
#    To update square, we can call set_square that takes square location, side_color, and chess_piece that's now
#    going to occupy it. Side_color and chess_piece can both be None, if the square is now empty. It will also be
#    updated.
#
# 4. Determining if a regular move is valid: Once make_move is called, it calls is_move_legal, which takes the original
#    square moving from and the destination square locations. Checks if original square has opponent piece color,
#    and if so returns False. Otherwise, checks the chess piece in the original square and makes sure the change in
#    location is legal for that piece type. If not legal or other pieces in its path, returns False.
#    Otherwise, returns True.
#    To check what's in square, we call get_square, returns {"location": [color side occupying, chess piece]} or None,
#    where we can access the necessary information in the value (list) of the 'location' key.
#
# 5. Determining if a capture is valid: After make_move calls is_move_legal and ensures chess piece can move in that way
#    make_move will only update white_side or black_side current score if destination square contained an opponent's
#    chess piece.
#
# 6. Determining the current state of the game: The get_game_state does this for us by checking data members white_side
#    and black_side (WhiteSide and BlackSide objects) to see if any of the collected chess pieces in their score
#    contains all of the opponent's chess pieces for that type.
#    The score for each side is set up like: {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}
#    We know there are 8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen, and 1 king that can be captured per side.
#    The method then returns 'UNFINISHED' if we did not find any piece has been completely captured, or 'WHITE_WON' or
#    'BLACK_WON' if we did.

def main():
    game = ChessVar()
    game.display_board()


if __name__ == '__main__':
    main()