# import Button class
from cmath import pi
from tkinter import Button
# import Random library
import random
import settings

# create class for Cell
class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append object to Cell.all list
        Cell.all.append(self)

    def create_button_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x}, {self.y}"
        )
        # create action for left-clicking
        btn.bind('<Button-1>', self.left_click_actions)
        # create action for right-clicking
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    # create method to define action for left-clicking
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked")

    # create method to define action for right-clicking
    def right_click_actions(self, event):
        print(event)
        print("I am right clicked")

    # create static method to convert some cells into mines
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        # create for loop to change the randomized picked cells into mines
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # format representation of each object with cell x,y values
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"