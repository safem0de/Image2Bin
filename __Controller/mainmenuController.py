import base64
from pathlib import Path
from tkinter import Label
import tkinter.filedialog as fd
import numpy as np
from PIL import Image, ImageTk

class mainmenuController:
    def __init__(self, view):
        self.view = view

    def OpenFile(self):
        dir = fd.askopenfilename() 
        return Path(dir)

    def Convert2Bin(self,img):
        with open(img, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())

        return converted_string

    def CreateBinText(self, image):
        Txtlist = []
        # with open('encode.bin', "w") as file:
        # with open(directory, "rb") as image:
        # a = image.read()
        data = (repr(image))

        data = data[2:]  #trim out the b'
        data = data[:-1]  #trim out the last '

        dataList = data.split('\\x')  #split by hex unit
        dataList = dataList[1:] #remove the blank  value at the beginning

        totalLen = len(dataList)

        i = 0
        hexline = ''
        lenCount = 0
        groupCount = 0
        for hex in dataList:
            if(lenCount == totalLen-1):
                hexline += '\\x' + hex
                # print('b\'' + hexline + '\'')
                Txtlist.append('b\'' + hexline + '\'')
                # file.write('b\'' + hexline + '\'')
                # file.write('\n')
            if(i == 16):  #change number of grouping here       
                # print('b\'' + hexline + '\'')
                Txtlist.append('b\'' + hexline + '\'')
                # file.write('b\'' + hexline + '\'')
                # file.write('\n')
                i=0
                hexline = ''
                groupCount += 1

            hexline += '\\x' + hex
            i+=1         
            lenCount += 1

        return Txtlist