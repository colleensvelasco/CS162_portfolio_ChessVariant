# Author: Colleen S. H. Velasco
# GitHub username: colleensvelasco
# Date: November 27, 2023
# Description: A program that is a chess game variant where the chess pieces move the same as they do in real chess,
#              but without castling, en passant, and pawn promotion. The first player side to capture all the
#              opponent's pieces of one chess piece type wins.

class ChessVar:
    """Represents a variant of chess consisting of a game board, white side, black side, current turn of
    the game, and round number. To win the game, one side must capture all of an opponent's pieces of one type."""

    def __init__(self):
        """Creates a ChessVar game with a board, black and white sides, a current turn (side), and round number.
        Initializes board as empty list and white_side as an object of WhiteSide class and black_side as an object
        of BlackSide class. Current turn is initialized to white. Round number initialized to 1."""
        self._board = []
        self._white_side = WhiteSide()
        self._black_side = BlackSide()
        self._current_turn = "white"
        self._round_number = 1

    def create_game_board(self):
        """Creates starting game board 8x8 (rows 1-8) and (columns a-h) consisting of 8 lists (each with 8 elements)
        within the board (an empty list initially). If a square is empty, it is occupied with a "-" in the list.
        For an occupied square, it contains {"location": [color side occupying, chess piece]}.
        For example: {"c2":["white", "pawn"]}"""
        pass


    def display_board(self):
        """Prints current board. Iterates through board and prints what each square contains."""
        pass

    def get_game_state(self):
        """Checks for the state of the game and returns 'UNFINISHED', 'WHITE_WON', or 'BLACK_WON.' A
        side wins when one has captured all of an opponent's pieces of one type. Checks white side and black side
        (WhiteSide and BlackSide objects) to see if any of the collected chess pieces in their score contains
        all of that kind."""
        pass

    def turn_changer(self):
        """Checks whose current_turn it is (black or white) and switches current_turn to other side. Every time black
        makes a move we finish a round, so we update round_number when current_turn changes from 'black' to 'white.'"""
        pass

    def set_square(self, sq_location, side_color, chess_piece):
        """Takes square location and the side color and chess piece that will occupy the given square and updates it.
        Side color and chess piece can be None if square is now empty."""
        pass

    def get_square(self, sq_location):
        """Takes square location string and returns what's contained in that square. If square has "-"
        square is empty and returns None."""
        pass

    def is_move_legal(self, original_sq, destination_sq):
        """Takes the square moved from (original_sq) and square moved to (destination_sq) and checks if original_sq
        has opponent's piece, and if so returns False. Otherwise, checks the chess piece in the original_sq and
        makes sure the change in location is legal for that piece type. If not legal or other pieces in path,
        returns False. Otherwise, returns True. To check what's in square, calls get_square."""
        # If it's the first move, pawn can move forward two spaces
        pass

    def make_move(self, original_sq, destination_sq):
        """Takes strings representing square moved from and square moved to. If square moved from has
        opponent's piece, illegal move attempted (calls is_move_legal to check), or game is over
        (calling get_game_state), returns False. Otherwise, makes indicated move and removes captured piece (if any)
        (calling set_square to do so), updates score (if needed), update whose turn (turn_changer), and returns True."""
        pass


class BlackSide:
    """Represents the black side of the chess variant game."""

    def __init__(self):
        """Creates the BlackSide of the chess variant game with a score (dictionary where keys= chess pieces and
        values= number of opponent pieces collected (initialized to 0)."""
        self._score = {"pawn": 0, "rook": 0, "knight": 0, "bishop": 0, "queen": 0, "king": 0}

    def set_score(self, piece_collected):
        """Takes name of chess piece collected (string) and updates BlackSide's score."""
        pass

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
        pass

    def get_score(self):
        """Returns WhiteSide score."""
        return self._score


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