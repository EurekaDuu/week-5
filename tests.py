import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_x_wins_in_first_row(self):
        board = [
            ['X', 'X', 'X'],
            [None, 'O', None],
            [None, 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_second_row(self):
        board = [
            [None, 'O', None],
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_third_row(self):
        board = [
            [None, 'O', None],
            [None, 'O', 'O'],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_first_col(self):
        board = [
            ['X', None, None],
            ['X', 'O', None],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_second_col(self):
        board = [
            [None, 'X', None],
            ['O', 'X', 'X'],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_third_col(self):
        board = [
            [None, 'O', 'X'],
            [None, 'O', 'X'],
            ['O', None, 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_diagonal(self):
        board = [
            ['X', 'O', None],
            [None, 'X', 'O'],
            ['O', None, 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    def test_x_wins_in_reverse_diagonal(self):
        board = [
            [None, 'O', 'X'],
            [None, 'X', 'O'],
            ['X', None, 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')
    # TODO: Test all functions from logic.py!
    def test_o_wins_in_first_row(self):
        board = [
            ['O', 'O', 'O'],
            [None, 'X', None],
            [None, 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_second_row(self):
        board = [
            [None, 'X', None],
            ['O', 'O', 'O'],
            [None, 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_third_row(self):
        board = [
            [None, 'X', None],
            [None, 'X', 'X'],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_first_col(self):
        board = [
            ['O', None, None],
            ['O', 'X', None],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_second_col(self):
        board = [
            [None, 'O', None],
            ['X', 'O', 'O'],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_third_col(self):
        board = [
            [None, 'X', 'O'],
            [None, 'X', 'O'],
            ['X', None, 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_diagonal(self):
        board = [
            ['O', 'X', None],
            [None, 'O', 'X'],
            ['X', None, 'O'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')
    def test_o_wins_in_reverse_diagonal(self):
        board = [
            [None, 'X', 'O'],
            [None, 'O', 'X'],
            ['O', None, 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'O')

    def test_draw(self):
        board = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'Draw')
    def test_no_result(self):
        board = [
            ['X', 'O', None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.get_winner(board), None)

    def test_make_empty_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(logic.make_empty_board(), board)
    def test_update_board(self):
        board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        updated_board = [
            ['X', None, None],
            [None, None, None],
            [None, None, None],
        ]
        logic.update_board(board, 0, 0, 'X')
        self.assertEqual(board, updated_board)
    def test_update_x_to_o(self):
        self.assertEqual(logic.other_player('X'), 'O')
    def test_update_o_to_x(self):
        self.assertEqual(logic.other_player('O'), 'X')
if __name__ == '__main__':
    unittest.main()
