from enum import Enum, auto
from position import Position

# Initial robot position that is not yet placed on the table
# Used (-1,-1) to invalidate commands before PLACE
INIT_ROBOT_POS = Position(-1, -1)

DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']

OFFSET_POS = {
    "NORTH": Position(0, 1),
    "SOUTH": Position(0, -1),
    "EAST": Position(1, 0),
    "WEST": Position(-1, 0),
}


class Robot:

    def __init__(self, table_end_pos):
        if table_end_pos.x < 0 or table_end_pos.y < 0:
            raise ValueError("Invalid table size!")
        self.table_end_pos = table_end_pos
        self.position = INIT_ROBOT_POS
        self.direction = "NORTH"

    def place(self, place_pos, direction):
        if place_pos.is_on_table(self.table_end_pos) and direction in DIRECTIONS:
            self.position = place_pos
            self.direction = direction

    def move(self):
        if self.position.is_on_table(self.table_end_pos):
            new_position = self.position + OFFSET_POS[self.direction]
            if new_position.is_on_table(self.table_end_pos):
                self.position = new_position

    def _rotate(self, turn_val=1):
        current_direction_index = DIRECTIONS.index(self.direction)
        # if count is positive then rotation is clockwise, if negative then counter
        new_direction_index = (current_direction_index + turn_val) % len(DIRECTIONS)
        self.direction = DIRECTIONS[new_direction_index]

    def turn_right(self):
        self._rotate(turn_val=1)

    def turn_left(self):
        self._rotate(turn_val=-1)

    def report(self):
        if self.position.is_on_table(self.table_end_pos):
            print(f'output: {self.position.x},{self.position.y},{self.direction}')
