import unittest

from robot import Robot
from position import Position

DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
# this sets a default 5x5 table
TABLE_END_POS = Position(4, 4)
VALID_ROBOT = Robot(TABLE_END_POS)


class TestRobotTurns(unittest.TestCase):
    def testRotate(self):
        VALID_ROBOT.place(Position(0, 0), 'NORTH')
        self.assertEqual(VALID_ROBOT.direction, 'NORTH')
        VALID_ROBOT._rotate(1)
        self.assertEqual(VALID_ROBOT.direction, 'EAST')
        VALID_ROBOT._rotate(-1)
        self.assertEqual(VALID_ROBOT.direction, 'NORTH')

    def testLeftTurns(self):
        # Tests all directions using left turn
        VALID_ROBOT.place(Position(0, 0), 'NORTH')
        self.assertEqual(VALID_ROBOT.direction, 'NORTH')
        for direction in [
            "WEST",
            "SOUTH",
            "EAST",
            "NORTH"
        ]:
            VALID_ROBOT.turn_left()
            self.assertEqual(VALID_ROBOT.direction, direction)

    def testRightTurns(self):
        VALID_ROBOT.place(Position(0, 0), "NORTH")
        # Check that robot does a 360 clockwise turn.
        self.assertEqual(VALID_ROBOT.direction, "NORTH")
        for direction in [
            "EAST",
            "SOUTH",
            "WEST",
            "NORTH"
        ]:
            VALID_ROBOT.turn_right()
            self.assertEqual(VALID_ROBOT.direction, direction)


class TestMovement(unittest.TestCase):
    def testValidMoveNorth(self):
        VALID_ROBOT.place(Position(2, 2), "NORTH")
        self.assertEqual(VALID_ROBOT.direction, "NORTH")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "NORTH")
        self.assertEqual(str(VALID_ROBOT.position), "(2,3)")

    def testValidMoveEast(self):
        VALID_ROBOT.place(Position(2, 2), "EAST")
        self.assertEqual(VALID_ROBOT.direction, "EAST")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "EAST")
        self.assertEqual(str(VALID_ROBOT.position), "(3,2)")

    def testValidMoveSouth(self):
        VALID_ROBOT.place(Position(2, 2), "SOUTH")
        self.assertEqual(VALID_ROBOT.direction, "SOUTH")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "SOUTH")
        self.assertEqual(str(VALID_ROBOT.position), "(2,1)")

    def testValidMoveWest(self):
        VALID_ROBOT.place(Position(2, 2), "WEST")
        self.assertEqual(VALID_ROBOT.direction, "WEST")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "WEST")
        self.assertEqual(str(VALID_ROBOT.position), "(1,2)")

    def testInvalidMoveNorth(self):
        VALID_ROBOT.place(Position(2, 4), "NORTH")
        self.assertEqual(VALID_ROBOT.direction, "NORTH")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "NORTH")
        self.assertEqual(str(VALID_ROBOT.position), "(2,4)")

    def testInvalidMoveEast(self):
        VALID_ROBOT.place(Position(4, 2), "EAST")
        self.assertEqual(VALID_ROBOT.direction, "EAST")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "EAST")
        self.assertEqual(str(VALID_ROBOT.position), "(4,2)")

    def testInvalidMoveSouth(self):
        VALID_ROBOT.place(Position(2, 0), "SOUTH")
        self.assertEqual(VALID_ROBOT.direction, "SOUTH")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "SOUTH")
        self.assertEqual(str(VALID_ROBOT.position), "(2,0)")

    def testInvalidMoveWest(self):
        VALID_ROBOT.place(Position(0, 2), "WEST")
        self.assertEqual(VALID_ROBOT.direction, "WEST")
        VALID_ROBOT.move()
        self.assertEqual(VALID_ROBOT.direction, "WEST")
        self.assertEqual(str(VALID_ROBOT.position), "(0,2)")


class TestPlacement(unittest.TestCase):

    def testInvalidPlacements(self):
        invalid_places = [(-2, -2), (-2, -1), (-1, -2), (-1, 5), (5, -1), (5, 5)]
        # Initialized robot is off-table
        robot = Robot(TABLE_END_POS)
        self.assertFalse(robot.position.is_on_table(TABLE_END_POS))
        for invalid in invalid_places:
            robot.place(Position(*invalid), "NORTH")
            self.assertFalse(robot.position.is_on_table(TABLE_END_POS))
        robot.place(Position(0, 0), "NORTH")
        self.assertTrue(robot.position.is_on_table(TABLE_END_POS))
        for invalid in invalid_places:
            robot.place(Position(*invalid), "NORTH")
            self.assertTrue(robot.position.is_on_table(TABLE_END_POS))

    def testInvalidTableSizes(self):
        for invalid in [(-2, -2), (-1, -1), (0, -1), (-1, 0)]:
            with self.assertRaises(ValueError):
                Robot(Position(*invalid))

    def testValidTableSizes(self):
        for valid in [(1, 1), (1, 2), (2, 1), (5, 5), (50, 50), (1, 50)]:
            Robot(Position(*valid))


if __name__ == '__main__':
    unittest.main()
