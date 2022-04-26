# import everything from the tkinter library
from tkinter import *
# import settings.py
import settings
# import utilities.py
import utilities

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
    bg='red', # change later to black after debugging
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
    bg='blue', # change to black after debugging
    # set width to 25% by calling width_prct()
    width=utilities.width_prct(25),
    # set height to 75% by calling height_prct()
    height=utilities.height_prct(75)
)
#place left_frame in window
left_frame.place(x=0, y=utilities.height_prct(25))

# Run the game window
root.mainloop()

