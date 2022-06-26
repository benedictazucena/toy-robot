# **Toy Robot**
Toy Robot - Iress Code Challenge


## Requirements

- python 3.6+

## Initial setup

  - Install Python3 - [Installation Guide](http:/https://docs.python-guide.org/starting/installation// "Installation Guide")
  - Install Git - [Installation Guide](https://github.com/git-guides/install-git "Installation Guide")
  - git clone git@github.com:benedictazucena/toy-robot.git

## Quick Start
1. Navigate first to to the toy-robot project folder.

1. Run this command to start the application in manual command input:
`$ python robot_app.py 5 5`
*Note: The arguments 5 5 are the dimensions (x,y) of the table to be used*

1. You may also use fileinput by specifying the flag -f and filename.
`$ python robot_app.py 5 5 -f commands.txt`
</table>

1. You may now use the `PLACE X,Y,F | LEFT | RIGHT | MOVE | REPORT` commands as specified in the challenge document.

## Sample Usage
Manual input usage:

    python robot_app.py 5 5
    Type commands: PLACE x,y,direction|MOVE|RIGHT|LEFT|REPORT
    PLACE 0,0,NORTH
    MOVE
    RIGHT
    MOVE
    REPORT
    output: 1,1,EAST

Command file usage:
    > python3 robot_app.py 5 5 -f commands.txt 
    output: 1,4,EAST
    output: 3,2,SOUTH
    output: 3,0,EAST
    output: 2,0,EAST


## Running Tests

  On the CLI under the toy-robot folder, run: `python -m unittest fnctest_robot_app.py` 


