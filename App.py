import tempfile
import tkinter as tk

from __Views.Mainmenu import mainMenu
from __Controller.mainmenuController import mainmenuController
from __Views.Images import ICON

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Image to Binary by Safem0de')
        self.geometry('+10+10')
        self.iconbitmap(default=ICON_PATH)
        self.resizable(0,0)

        ### create a view and place it on the root window
        view = mainMenu(self)
        view.grid(row=0, column=0)

        ### create a controller
        controller = mainmenuController(view)

        ### set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()