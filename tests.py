import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_x_wins_in_first_row(self):
        game = logic.Game()
        game.board = [
            ['X', 'X', 'X'],
            [None, 'O', None],
            [None, 'O', 'O'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_second_row(self):
        game = logic.Game()
        game.board = [
            [None, 'O', None],
            ['X', 'X', 'X'],
            [None, 'O', 'O'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_third_row(self):
        game = logic.Game()
        game.board = [
            [None, 'O', None],
            [None, 'O', 'O'],
            ['X', 'X', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_first_col(self):
        game = logic.Game()
        game.board = [
            ['X', None, None],
            ['X', 'O', None],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_second_col(self):
        game = logic.Game()
        game.board = [
            [None, 'X', None],
            ['O', 'X', 'X'],
            [None, 'X', 'O'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_third_col(self):
        game = logic.Game()
        game.board = [
            [None, 'O', 'X'],
            [None, 'O', 'X'],
            ['O', None, 'X'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_diagonal(self):
        game = logic.Game()
        game.board = [
            ['X', 'O', None],
            [None, 'X', 'O'],
            ['O', None, 'X'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_x_wins_in_reverse_diagonal(self):
        game = logic.Game()
        game.board = [
            [None, 'O', 'X'],
            [None, 'X', 'O'],
            ['X', None, 'O'],
        ]
        self.assertEqual(game.get_winner(), 'X')
    def test_o_wins_in_first_row(self):
        game = logic.Game()
        game.board = [
            ['O', 'O', 'O'],
            [None, 'X', None],
            [None, 'X', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_second_row(self):
        game = logic.Game()
        game.board = [
            [None, 'X', None],
            ['O', 'O', 'O'],
            [None, 'X', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_third_row(self):
        game = logic.Game()
        game.board = [
            [None, 'X', None],
            [None, 'X', 'X'],
            ['O', 'O', 'O'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_first_col(self):
        game = logic.Game()
        game.board = [
            ['O', None, None],
            ['O', 'X', None],
            ['O', 'X', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_second_col(self):
        game = logic.Game()
        game.board = [
            [None, 'O', None],
            ['X', 'O', 'O'],
            [None, 'O', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_third_col(self):
        game = logic.Game()
        game.board = [
            [None, 'X', 'O'],
            [None, 'X', 'O'],
            ['X', None, 'O'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_diagonal(self):
        game = logic.Game()
        game.board = [
            ['O', 'X', None],
            [None, 'O', 'X'],
            ['X', None, 'O'],
        ]
        self.assertEqual(game.get_winner(), 'O')
    def test_o_wins_in_reverse_diagonal(self):
        game = logic.Game()
        game.board = [
            [None, 'X', 'O'],
            [None, 'O', 'X'],
            ['O', None, 'X'],
        ]
        self.assertEqual(game.get_winner(), 'O')

    def test_draw(self):
        game = logic.Game()
        game.board = [
            ['X', 'X', 'O'],
            ['O', 'O', 'X'],
            ['X', 'O', 'X'],
        ]
        self.assertEqual(game.get_winner(), 'Draw')
    def test_no_result(self):
        game = logic.Game()
        game.board = [
            ['X', 'O', None],
            [None, None, None],
            [None, None, None],
        ]
        self.assertEqual(game.get_winner(), None)
    def test_update_board(self):
        game = logic.Game()
        game.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
        updated_board = [
            ['X', None, None],
            [None, None, None],
            [None, None, None],
        ]
        game.update_board(0, 0, 'X')
        self.assertEqual(game.board, updated_board)
    def test_update_x_to_o(self):
        game = logic.Game()
        self.assertEqual(game.other_player('X'), 'O')
    def test_update_o_to_x(self):
        game = logic.Game()
        self.assertEqual(game.other_player('O'), 'X')
    def test_get_bot_input(self):
        game = logic.Game()
        game.board = [
            [None, 'X', 'O'],
            [None, 'O', 'X'],
            ['O', None, 'X'],
        ]
        x, y = game.get_bot_input()
        coor_set = [[0, 0], [1, 0], [2, 1]]
        self.assertEqual([x, y] in coor_set, True)
if __name__ == '__main__':
    unittest.main()
