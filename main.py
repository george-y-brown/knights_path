
import knights

board_size = 8 # not defined by user but can be increased in size to 26 without modifying inputs.

start_pos = knights.validate_input(board_size=board_size, input_type='start')
target_pos = knights.validate_input(board_size=board_size, input_type='target')

path, distance = knights.find_path(start=start_pos, target=target_pos, board_size = board_size)
print(' '.join(path))
out = input('press any key to close...')