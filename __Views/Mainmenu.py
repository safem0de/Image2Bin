from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
import tkinter.scrolledtext as sc
import os
from __Controller.mainmenuController import mainmenuController

class mainMenu(ttk.Frame):
    
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label

        self.Import_Button = ttk.Button(self, text='Import Image', command=lambda: self.Import_ImageClick())
        self.Import_Button.grid(row=0, column=0)

        self.frame = Frame(self)
        self.frame.grid(row=1, column=0)

        self.img = Label(self.frame)
        self.img.place(x=0, y=0)
        self.img.grid(row=0, column=0)

        self.Text_area = sc.ScrolledText(self, width=80, height=40, wrap=tk.WORD)
        self.Text_area.grid(row=2, column=0)

        # Text_area.insert(tk.END,'ทดสอบ')


    def set_controller(self, controller:mainmenuController):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    ### https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/
    def Import_ImageClick(self):
        x = os.path.normpath(self.controller.OpenFile())

        self.load = Image.open(x)
        y = max(self.load.width,self.load.height)
        if y > 200:
            ratio = 200/y
            resized_image = self.load.resize((int(self.load.width*ratio),int(self.load.height*ratio)), Image.ANTIALIAS)
            self.render = ImageTk.PhotoImage(resized_image)
            self.img.config(image=self.render)

            data = resized_image.tobytes()
            values = self.controller.CreateBinText(data)
            for v in values:
                self.Text_area.insert(tk.END, v+'\n')
        else:
            self.render = ImageTk.PhotoImage(self.load)
            self.img.config(image=self.render)

            data = self.load.tobytes()
            values = self.controller.CreateBinText(data)
            for v in values:
                self.Text_area.insert(tk.END, v+'\n')

        copy = self.Text_area.get('1.0', tk.END).strip()
        self.clipboard_clear()
        self.clipboard_append(copy)
        self.update()