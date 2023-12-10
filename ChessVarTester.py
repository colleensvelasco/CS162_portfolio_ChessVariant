
import unittest
import string
from ChessVar import ChessVar, BlackSide, WhiteSide, ChessPieceMove, PawnMove
from ChessVar import RookMove, KnightMove, BishopMove, QueenMove, KingMove

class TestChessVar(unittest.TestCase):

    def test_1(self):
        """Tests get_current_turn method from ChessVar class."""
        today_game = ChessVar()
        self.assertEqual(today_game.get_current_turn(), "white")

    def test_2(self):
        """Tests get_current_turn and turn_changer methods from ChessVar class."""
        today_game = ChessVar()
        today_game.turn_changer()
        self.assertEqual(today_game.get_current_turn(), "black")

    def test_3(self):
        """Tests create_game_board and get_square methods for empty square from ClassVar class."""
        today_game = ChessVar()
        today_game.create_game_board()
        # Returns None is sq is empty.
        self.assertIsNone(today_game.get_square("d5"))

    def test4(self):
        """Tests create_game_board and get_square methods for occupied square from ClassVar class."""
        today_game = ChessVar()
        today_game.create_game_board()
        # Returns [color, chess piece] is sq is occupied.
        self.assertEqual(today_game.get_square("c2"), ["white", "pawn"])

    def test5(self):
        """Tests set_square for now empty square for class ChessVar."""
        today_game = ChessVar()
        today_game.create_game_board()
        today_game.set_square("e1", None, None)
        # Empties square
        self.assertIsNone(today_game.get_square("e1"))

    def test6(self):
        """Tests set_square for empty square, now occupied for class ChessVar."""
        today_game = ChessVar()
        today_game.create_game_board()
        today_game.set_square("d4", "white", "knight")
        # Empty square is now occupied
        self.assertEqual(today_game.get_square("d4"), ["white", "knight"])

    def test7(self):
        """Tests set_square for previously occupied square, now occupied with different piece for class ChessVar."""
        today_game = ChessVar()
        today_game.create_game_board()
        today_game.set_square("d7", "white", "knight")
        # Occupied square is now occupied with another piece
        self.assertEqual(today_game.get_square("d7"), ["white", "knight"])

    def test8(self):
        """Tests is_move_legal and make_move (ChessVar methods) for pawn and is_move_valid (PawnMove method)."""
        today_game = ChessVar()
        today_game.create_game_board()
        self.assertTrue(today_game.make_move("e2", "e4"))

    def test9(self):
        """Tests is_move_legal and make_move (Chess methods) for"""

