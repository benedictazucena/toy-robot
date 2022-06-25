import sys
import re
import argparse
from robot import Robot
from position import Position

# Regex for validating PLACE syntax
PLACE_SYNTAX = re.compile(r'PLACE \d+,\d+,(NORTH|SOUTH|EAST|WEST)')


class Commander:

    def __init__(self, robot):
        self.robot = robot

    def execute(self, command):
        if "PLACE" in command:
            if PLACE_SYNTAX.match(command):
                place_values = command.split(" ")[1]
                x, y, direction = place_values.split(",")
                place_pos = Position(int(x), int(y))
                self.robot.place(place_pos, direction)

        elif command == 'MOVE':
            self.robot.move()
        elif command == 'LEFT':
            self.robot.turn_left()
        elif command == 'RIGHT':
            self.robot.turn_right()
        elif command == 'REPORT':
            self.robot.report()
        else:
            pass  # Ignore any invalid command lines.


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Toy Robot Input Parse")
    parser.add_argument('table_x', type=int, help='Table width; x units ')
    parser.add_argument('table_y', type=int, help='Table length; y units')
    parser.add_argument("--file", "-f", help="Use a text file as set of commands")
    args = parser.parse_args()
    table_x = args.table_x
    table_y = args.table_y

    if table_x <= 0 or table_y <= 0:
        raise ValueError("Invalid table size!")

    table_end_pos = Position(table_x - 1, table_y - 1)
    robot = Robot(table_end_pos)
    robot_commander = Commander(robot)

    if args.file:
        try:
            command_file = open(args.file)
            for line in command_file:
                command = line.strip()
                robot_commander.execute(command)
            sys.exit()
        except FileNotFoundError:
            print("Command file not valid. Proceeding with manual commands\n")

    active = True
    print("Type commands: PLACE x,y,direction|MOVE|RIGHT|LEFT|REPORT")
    while active:
        command = input().strip()
        if command == "q":
            print("closing app...")
            active = False

        robot_commander.execute(command)
