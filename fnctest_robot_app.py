#!/usr/bin/env python3.6

import io
import unittest

from robot_app import Commander
from robot import Robot
from position import Position

DIRECTIONS = ['NORTH', 'EAST', 'SOUTH', 'WEST']
TABLE_END_POS = Position(4,4)

class TestTurns(unittest.TestCase):

    def testLeftTurns(self):
        # Check that robot does a 360 counter-clockwise turn.
        robot = Robot(TABLE_END_POS)
        robot.place(Position(0, 0), 'NORTH')
        self.assertEqual(robot.direction, 'NORTH')
        for direction in [
            "WEST",
            "SOUTH",
            "EAST",
            "NORTH"
        ]:
            robot.turn_left()
            self.assertEqual(robot.direction, direction)

    def testRightTurns(self):
        robot = Robot(TABLE_END_POS)
        robot.place(Position(0, 0), "NORTH")
        # Check that robot does a 360 clockwise turn.
        self.assertEqual(robot.direction, "NORTH")
        for direction in [
            "EAST",
            "SOUTH",
            "WEST",
            "NORTH"
        ]:
            robot.turn_right()
            self.assertEqual(robot.direction, direction)


class TestPlacement(unittest.TestCase):

    def testInvalidPlacements(self):
        robot = Robot(TABLE_END_POS)
        invalid_places = [(-1, -1), (-1, 0), (0, -1), (0, 5), (5, 0), (5, 5)]
        # Check that robot ignores invalid placements.
        self.assertFalse(robot.position.is_on_table(TABLE_END_POS))
        for invalid in invalid_places:
            robot.place(Position(*invalid), "NORTH")
            self.assertFalse(robot.position.is_on_table(TABLE_END_POS))
        robot.place(Position(0, 0), "NORTH")
        # Thunderbirds Are Go!
        self.assertTrue(robot.position.is_on_table(TABLE_END_POS))
        # Check that robot ignores invalid placements after it's on the table.
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
