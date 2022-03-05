
from collections import deque
from random import randint

class Location() :

    def __init__(self, position_x: int = 0, position_y: int = 0, distance: int = 0, previous_location = None) -> None :
        self.position_x = position_x
        self.position_y = position_y
        self.distance = distance
        self.previous_location = previous_location # create pseudo linked list for back tracing

    def set_coords(self, position: str) -> None :
        
        # Use ASCII index for alpha -> numeric conversion but offset for 0 index
        self.position_x = ord(position[0].lower()) - 97
        self.position_y = int(position[1:]) - 1

    def coords_to_position(self) -> str :

        # Use ASCII index for numeric -> alpha conversion
        return chr(self.position_x + 97).upper() + str(self.position_y + 1)

def valid_move(position_x: int, position_y: int, board_size: int) -> bool :
    
    # Check no position exceeds boards limits using 0 index
    if position_x < 0 or position_y < 0 or position_x >= board_size or position_y >= board_size :
        return False
    return True

def suggest_random(board_size: int) -> str :

    rand_x = randint(0, board_size -1)
    rand_y = randint(0, board_size -1)
    rand_loc = Location(position_x=rand_x, position_y=rand_y)
    suggestion = rand_loc.coords_to_position()

    return suggestion

def validate_input(board_size: int, input_type: str, optional_loc: str=None) -> Location :
    """
    Check input is alphanumeric and does not exceed maximum length.
    Current maximum length of x-axis is 26
    """
    if board_size < 6 or board_size > 26 :
        print('board must be between 6 and 26 squares')
        raise Exception # board size cannot be modified by user - raise exception to show error if changed by dev

    while True :
        if optional_loc :
            position = optional_loc
        else :
            suggestion = suggest_random(board_size=board_size)
            position = input(f"Enter {input_type} position for a board of {board_size} squares e.g. {suggestion}: ")
            
        # check alphanumeric and not invalid length
        if position.isalnum() and len(position) <= len(str(board_size)) * 2 :
            try :
                y_pos = int(position[1:])
            except ValueError :
                print('invalid coordinates')
                continue
            if ord(position[0].lower()) - 97 > board_size :
                print('invalid x coordinate')
                continue
            if y_pos <= board_size and y_pos >= 0 :
                break
            else :
                print('invalid y coordinate')
        print('invalid coordinates')

    valid_position = Location()
    valid_position.set_coords(position)
    if input_type == 'start' :
        valid_position.previous_location = valid_position.coords_to_position()
    return valid_position

def track_back(loc_node: Location) -> tuple :
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
            return path, distance

    return 'unable to find path', 0
    

def find_path(start: Location, target: Location, board_size: int) -> tuple :
    """
    Takes the starting position as head node of pseudo linked list and 
    puts all possible moves into a queue.
    """
    existing_loc = []
    queue = deque()
    queue.append(start)

    while queue :
        loc_node = queue.popleft()

        if loc_node.position_x == target.position_x and loc_node.position_y == target.position_y :
            shortest_path, shortest_distance = track_back(loc_node)
            return shortest_path, shortest_distance

        if loc_node not in existing_loc :

            #ensure locations are remembered to prevent infinite loop
            existing_loc.append(loc_node)

            #all possible combinations of move
            move_options = [[2,-1], [2,1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]

            for move in move_options :
                move_x = loc_node.position_x + move[0]
                move_y = loc_node.position_y + move[1]

                if valid_move(position_x=move_x, position_y=move_y, board_size=board_size) :
                    queue.append(Location(position_x=move_x, position_y=move_y, distance = loc_node.distance + 1, previous_location = loc_node))

    return 'unable to find path', 0