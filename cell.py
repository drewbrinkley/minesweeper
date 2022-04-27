# import Button class
from cmath import pi
from tkinter import Button, Label
# import Random library
import random
import settings

# create class for Cell
class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
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
        )
        # create action for left-clicking
        btn.bind('<Button-1>', self.left_click_actions)
        # create action for right-clicking
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    # create static method to display number of cells remaining
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left:{Cell.cell_count}",
            width=12,
            height=4,
            bg="black",
            fg='white',
            font=("", 30)
        )
        Cell.cell_count_label_object = lbl
    
    # create method to define action for left-clicking
    def left_click_actions(self, event):
        # create if statement for result if cell is a mine
        if self.is_mine:
            self.show_mine()
        # else statement for result if cell is not a mine
        else:
            # create if statement to show all surrounding cells if selected cell has no adjacent mines
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

    # create method get_cell_by_axis to return the cell object based on the values of x,y
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    # create read-only attribute to return list of possible surrounding cells
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x -1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y -1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1)
        ]

        # create list comprehension with one-line for loop to disregard null cell values
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    # create read-only attribute with method to show mine count of surrounding cells
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter
    
    # create method show_cell that shows number of mines in surrounding cells
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # replace the text of cell_count_label with updated count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left:{Cell.cell_count}"
                    )
        # change status of is_opened of selected cell to mark it as opened
        self.is_opened = True

    # create method show_mine for selected cells with mines
    def show_mine(self):
        #  logic to interrupt game and display "game over" message
        self.cell_btn_object.configure(bg='red') # temporarily change cell to red

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