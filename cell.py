# import Button class
from tkinter import Button

# create class for Cell
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_button_object(self, location):
        btn = Button(
            location,
            text='Text'
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