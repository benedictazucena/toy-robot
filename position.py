class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, position):
        return Position(self.x + position.x, self.y + position.y)

    def is_on_table(self, table_end_pos):
        if 0 <= self.x <= table_end_pos.x and 0 <= self.y <= table_end_pos.y:
            return True
        return False
