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
        self.cell_btn_object = btn