# Author: Colleen S. H. Velasco
# GitHub username: colleensvelasco
# Date: November 27, 2023
# Description:

class ChessVar:
    """"""

    def __init__(self):
        """Creates a ChessVar game with a board, black and white sides, and a current turn (side).
        Initializes board as empty list and white_side as an object of WhiteSide class and black_side as an object
        of BlackSide class. Current turn is initialized to None."""
        self._board = []
        self._white_side = WhiteSide()
        self._black_side = BlackSide()
        self._current_turn = None

    def create_game_board(self):
        """Creates starting game board 8x8 (rows 1-8) and (columns a-h) consisting of 8 lists (each with 8 elements)
        within the board (an empty list initially)."""
        for list_for_row in range(8):
            row = []
            if list_for_row == 0:
                # Creating first row: black side's row of rooks, knights, bishops, queen, and king

    def display_board(self):
        """Prints current board."""

    def get_game_state(self):
        """Checks for the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON.' A
        side wins when one has captured all of an opponent's pieces of one type."""

    def turn_changer(self):
        """Checks whose current_turn it is (black or white) and switches current_turn to other side."""

    def set_square(self, sq_location, side_color, chess_piece):
        """Takes square location and the side color and chess piece that will occupy the given square and updates it.
        Side color and chess piece can be None if square is now empty."""

    def get_square(self, sq_location):
        """Takes square location string and returns the what's contained in that square. If square has "-"
        square is empty and returns None."""


    def make_move(self, original_sq, destination_sq):
        """Takes strings representing square moved from and square moved to and
        make indicated move and remove captured piece (if any) (calling square_changer to do so),
        updates score (if needed), update whose turn, and returns True. If square moved from has opponent's piece, illegal move attempted,
        or game is over, returns False."""
        # If it's the first move, pawn can move forward two spaces


class BlackSide:
    """Represents the black side of the chess variant game."""

    def __init__(self):
        """Creates the BlackSide of the chess variant game with a score (dictionary where keys= chess pieces and
        values= number of pieces collected (initialized to 0)."""
        self._score = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    def set_score(self, piece_collected):
        """Takes name of chess piece collected (string) and updates BlackSide's score."""

    def get_score(self):
        """Returns BlackSide score."""
        return self._score


class WhiteSide:
    """Represents the white side of the chess variant game."""

    def __init__(self):
        """Creates the WhiteSide of the chess variant game with a score (dictionary where keys= chess pieces and
        values= number of pieces collected (initialized to 0)."""
        self._score = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    def set_score(self, piece_collected):
        """Takes name of chess piece collected (string) and updates WhiteSide's score."""

    def get_score(self):
        """Returns WhiteSide score."""
        return self._score


class ChessPiece:
    """Represents a ChessPiece"""