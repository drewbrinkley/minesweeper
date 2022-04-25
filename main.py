# import everything from the tkinter library
from tkinter import *

import settings

# create root variable
root = Tk()
# change background color of game window
root.configure(bg="black")
# set size of game window, length x width
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
# add title to game window
root.title("Minesweeper Game")
# disallow resizing of game window
root.resizable(False, False)

# create variable top_frame, instantiated from Frame class - create frame at top of game window
top_frame = Frame(
    root,
    bg='red', # change later to black after debugging
    width=1440,
    height=180
)
# place top_frame in window
top_frame.place(x=0, y=0)

# create variable, left_frame, to create frame on left side of window
left_frame = Frame(
    root,
    bg='blue', # change to black after debugging
    width=360,
    height=540
)
#place left_frame in window
left_frame.place(x=0, y=180)

# Run the game window
root.mainloop()

