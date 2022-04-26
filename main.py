# import everything from the tkinter library
from tkinter import *
# import settings.py
import settings
# import utilities.py
import utilities
# import Cell class
from cell import Cell

# create root variable
root = Tk()
# change background color of game window
root.configure(bg="black")
# set size of game window, length x width are imported from settings
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# add title to game window
root.title("Minesweeper Game")
# disallow resizing of game window
root.resizable(False, False)

# create variable top_frame, instantiated from Frame class - create frame at top of game window
top_frame = Frame(
    root,
    bg='black', 
    # set WIDTH to 100%
    width=settings.WIDTH,
    # set height to 25% by calling height_prct() from utilities
    height=utilities.height_prct(25)
)
# place top_frame in window
top_frame.place(x=0, y=0)

# create variable, left_frame, to create frame on left side of window
left_frame = Frame(
    root,
    bg='black', 
    # set width to 25% by calling width_prct()
    width=utilities.width_prct(25),
    # set height to 75% by calling height_prct()
    height=utilities.height_prct(75)
)
#place left_frame in window
left_frame.place(x=0, y=utilities.height_prct(25))

# create variable, center_frame, to create frame in center of window
center_frame = Frame(
    root,
    bg='black', 
    # set dimensions to 75% by calling width_prct and height_prct
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)

# place center_frame in window
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

# nested for loops to create grid of cell/buttons
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

print(Cell.all)

# Run the game window
root.mainloop()

