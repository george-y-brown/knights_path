
from collections import deque

class Location() :

    def __init__(self, position_x: int = 0, position_y: int = 0, distance: int = 0, previous_location = None) -> None :
        self.position_x = position_x
        self.position_y = position_y
        self.distance = distance
        self.previous_location = previous_location # create pseudo linked list for back tracing

    def set_coords(self, position: str) -> None :
        
        # Use ASCII index for alpha -> numeric conversion but offset for 0 index
        self.position_x = ord(position[0].lower()) - 97
        self.position_y = int(position[1:])

    def coords_to_position(self) -> str :
        # Use ASCII index for numeric -> alpha conversion
        return chr(self.position_x + 97).upper() + str(self.position_y)

def valid_move(position_x: int, position_y: int, board_size: int) -> bool :
    
    # Check no position exceeds boards limits using 0 index
    if position_x < 0 or position_y < 0 or position_x >= board_size or position_y >= board_size :
        return False
    return True

def validate_input(board_size: int, input_type: str) -> Location :
    """
    Check input is alphanumeric and does not exceed maximum length.
    Current maximum length of x-axis is 26
    """
    if board_size < 6 or board_size > 26 :
        print('board must be between 6 and 26 squares')
        raise Exception

    while True :
        position = input(f"Enter {input_type} position for a board of {board_size} squares e.g. A1: ")

        # check alphanumeric and not invalid length
        if position.isalnum() and len(position) <= len(str(board_size)) * 2 :
            try :
                y_pos = int(position[1:]) - 1 #offset for 0 index
            except ValueError :
                print('invalid y coordinate')
                pass
            if ord(position[0].lower()) - 96 >= board_size :
                print('invalid x coordinate')
                pass
            if y_pos < board_size and y_pos >= 0 :
                break
            else :
                print('invalid y coordinate')
                pass

    valid_position = Location()
    valid_position.set_coords(position)
    if input_type == 'start' :
        valid_position.previous_location = valid_position.coords_to_position()
    return valid_position

def track_back(loc_node: Location) -> list :
    """
    Trace backwards from completed node to starting point
    """
    path = []
    distance = loc_node.distance
    while loc_node is not None :

        path.append(loc_node.coords_to_position())
        loc_node = loc_node.previous_location        

        if len(path) == distance + 1 :
            path.reverse()
            return path

    return 'unable to find path'
    

def find_path(start: Location, target: Location, board_size: int) -> tuple :

    existing_loc = []
    queue = deque()
    queue.append(start)

    while queue :
        loc_node = queue.popleft()

        if loc_node.position_x == target.position_x and loc_node.position_y == target.position_y :
            print(track_back(loc_node))
            return

        if loc_node not in existing_loc :

            #ensure locations are remembered to prevent infinite loop
            existing_loc.append(loc_node)

            #all possible combinations of move
            option_x = [2, 2, -2, -2, 1, 1, -1, -1]
            option_y = [-1, 1, 1, -1, 2, -2, 2, -2]

            for i in range(len(option_x)) :
                move_x = loc_node.position_x + option_x[i]
                move_y = loc_node.position_y + option_y[i]

                if valid_move(position_x=move_x, position_y=move_y, board_size=board_size) :
                    queue.append(Location(position_x=move_x, position_y=move_y, distance = loc_node.distance + 1, previous_location = loc_node))
       
board_size = 8 # not defined by user but can be increased in size to 26 without modifying inputs.

start_pos = validate_input(board_size=board_size, input_type='start')
target_pos = validate_input(board_size=board_size, input_type='target')
find_path(start=start_pos, target=target_pos, board_size = board_size)

out = input('press any key to close...')