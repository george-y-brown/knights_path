
import unittest
import knights

class TestKnights(unittest.TestCase) :

    def test_validate_input(self) :

        board_size = 8
        optional_loc = 'F5'

        location_start = knights.validate_input(board_size, input_type='start', optional_loc=optional_loc)
        location_target = knights.validate_input(board_size, input_type='target', optional_loc=optional_loc)
        expected_start = {'position_x': 5, 'position_y': 4, 'distance': 0, 'previous_location': optional_loc}
        expected_target = {'position_x': 5, 'position_y': 4, 'distance': 0, 'previous_location': None}
        self.assertEqual(expected_start, location_start.__dict__)
        self.assertEqual(expected_target, location_target.__dict__)
        self.assertEqual(optional_loc, location_start.coords_to_position())

    def test_find_path(self) :

        board_size = 8

        start_loc = knights.validate_input(board_size, input_type='start', optional_loc='A1')
        target_loc = knights.validate_input(board_size, input_type='target', optional_loc='C5')
        
        tested_path, tested_distance = knights.find_path(start_loc, target_loc, board_size)
        expected_path = ['A1', 'B3', 'C5']
        expected_distance = 2
        self.assertEqual(expected_path, tested_path)
        self.assertEqual(expected_distance, tested_distance)

    def test_valid_move(self) :

        board_size = 8

        expected_valid = knights.valid_move(position_x=0,position_y=6, board_size=board_size)
        expected_invalid = knights.valid_move(position_x=8,position_y=0, board_size=board_size)
        self.assertEqual(expected_valid, True)
        self.assertEqual(expected_invalid, False)

if __name__ == '__main__' :

    unittest.main()