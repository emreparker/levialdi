import tkinter.filedialog
from tkinter import messagebox
import numpy as np
import tkinter as tk
from tkinter.filedialog import *
from PIL import Image, ImageTk
import csv
from PIL import ImageGrab
from copy import deepcopy
import time

nccLevialdi = 0
iterationLevialdi = 0
openedImage=None
binaryImage=None
framedImage=None
pixelMapAsString=""
LevialdiCanvas = None


root = Tk()

def main():

    global root
    root.geometry("979x624+254+40")
    root.title("Emre Arslan Programming Studio Project 1")
    root.configure(background="salmon")

    root.LevialdiCanvas = tk.Canvas(root)
    root.LevialdiCanvas.place(relx=0.01, rely=0.112, relheight=0.838, relwidth=0.32)

    root.LevialdiCanvas.configure(background="#d9d9d9")
    root.LevialdiCanvas.configure(borderwidth="2")
    root.LevialdiCanvas.configure(insertbackground="black")
    root.LevialdiCanvas.configure(relief='ridge')
    root.LevialdiCanvas.configure(selectbackground="#c4c4c4")
    root.LevialdiCanvas.configure(selectforeground="black")
    root.LevialdiCanvas.configure(width=313)

    root.Open = tk.Button(root)
    root.Open.place(relx=0.02, rely=0.032, height=34, width=77)
    root.Open.configure(activebackground="#ececec")
    root.Open.configure(activeforeground="#000000")
    root.Open.configure(background="#d9d9d9")
    root.Open.configure(disabledforeground="#a3a3a3")
    root.Open.configure(foreground="#000000")
    root.Open.configure(highlightbackground="#d9d9d9")
    root.Open.configure(highlightcolor="black")
    root.Open.configure(pady="0")
    root.Open.configure(text='''Open''')
    root.Open.configure(width=77)
    root.Open.configure(command=imageOpen())

    root.Reset = tk.Button(root)
    root.Reset.place(relx=0.123, rely=0.032, height=34, width=77)
    root.Reset.configure(activebackground="#ececec")
    root.Reset.configure(activeforeground="#000000")
    root.Reset.configure(background="#d9d9d9")
    root.Reset.configure(disabledforeground="#a3a3a3")
    root.Reset.configure(foreground="#000000")
    root.Reset.configure(highlightbackground="#d9d9d9")
    root.Reset.configure(highlightcolor="black")
    root.Reset.configure(pady="0")
    root.Reset.configure(text='''Reset''')
    root.Reset.configure(width=77)
    root.Reset.configure(command=lambda: reset(framedImage))

    root.TSF = tk.Button(root)
    root.TSF.place(relx=0.398, rely=0.16, height=24, width=207)
    root.TSF.configure(activebackground="#ececec")
    root.TSF.configure(activeforeground="#000000")
    root.TSF.configure(background="#d9d9d9")
    root.TSF.configure(disabledforeground="#a3a3a3")
    root.TSF.configure(foreground="#000000")
    root.TSF.configure(highlightbackground="#d9d9d9")
    root.TSF.configure(highlightcolor="black")
    root.TSF.configure(pady="0")
    root.TSF.configure(text='''TSF''')
    root.TSF.configure(width=207)

    root.LEV = tk.Button(root)
    root.LEV.place(relx=0.398, rely=0.112, height=24, width=207)
    root.LEV.configure(activebackground="#ececec")
    root.LEV.configure(activeforeground="#000000")
    root.LEV.configure(background="#d9d9d9")
    root.LEV.configure(disabledforeground="#a3a3a3")
    root.LEV.configure(foreground="#000000")
    root.LEV.configure(highlightbackground="#d9d9d9")
    root.LEV.configure(highlightcolor="black")
    root.LEV.configure(pady="0")
    root.LEV.configure(text='''Levialdi''')
    root.LEV.configure(width=207)
    root.LEV.configure(command= lambda: levialdi(framedImage))

    root.TSFCanvas = tk.Canvas(root)
    root.TSFCanvas.place(relx=0.684, rely=0.112, relheight=0.838, relwidth=0.299)
    root.TSFCanvas.configure(background="#d9d9d9")
    root.TSFCanvas.configure(borderwidth="2")
    root.TSFCanvas.configure(insertbackground="black")
    root.TSFCanvas.configure(relief='ridge')
    root.TSFCanvas.configure(selectbackground="#c4c4c4")
    root.TSFCanvas.configure(selectforeground="black")
    root.TSFCanvas.configure(width=293)

    root.itercounter = tk.Label(root)
    root.itercounter.place(relx=0.46, rely=0.048, height=31, width=54)
    root.itercounter.configure(background="#d9d9d9")
    root.itercounter.configure(disabledforeground="#a3a3a3")
    root.itercounter.configure(foreground="#000000")
    root.itercounter.configure(text='''''')
    root.itercounter.configure(width=54)

    root.ncccounter = tk.Label(root)
    root.ncccounter.place(relx=0.572, rely=0.048, height=31, width=54)
    root.ncccounter.configure(activebackground="#f9f9f9")
    root.ncccounter.configure(activeforeground="black")
    root.ncccounter.configure(background="#d9d9d9")
    root.ncccounter.configure(disabledforeground="#a3a3a3")
    root.ncccounter.configure(foreground="#000000")
    root.ncccounter.configure(highlightbackground="#d9d9d9")
    root.ncccounter.configure(highlightcolor="black")
    root.ncccounter.configure(text='''''')
    root.ncccounter.configure(width=54)

    root.ITER = tk.Message(root)
    root.ITER.place(relx=0.398, rely=0.048, relheight=0.053, relwidth=0.067)
    root.ITER.configure(background="#d9d9d9")
    root.ITER.configure(foreground="#000000")
    root.ITER.configure(highlightbackground="#d9d9d9")
    root.ITER.configure(highlightcolor="black")
    root.ITER.configure(text='''Iterations:''')
    root.ITER.configure(width=66)

    root.NCC = tk.Message(root)
    root.NCC.place(relx=0.531, rely=0.048, relheight=0.053, relwidth=0.043)
    root.NCC.configure(background="#d9d9d9")
    root.NCC.configure(foreground="#000000")
    root.NCC.configure(highlightbackground="#d9d9d9")
    root.NCC.configure(highlightcolor="black")
    root.NCC.configure(text='''NCC:''')
    root.NCC.configure(width=42)

    root.Binary = tk.Text(root)
    root.Binary.place(relx=0.358, rely=0.208, relheight=0.744, relwidth=0.3)
    root.Binary.configure(background="white")
    root.Binary.configure(font=("TkTextFont", 2))
    root.Binary.configure(foreground="black")
    root.Binary.configure(highlightbackground="#d9d9d9")
    root.Binary.configure(highlightcolor="black")
    root.Binary.configure(insertbackground="black")
    root.Binary.configure(selectbackground="#c4c4c4")
    root.Binary.configure(selectforeground="black")
    root.Binary.configure(width=294)
    root.Binary.configure(wrap='word')





    root.mainloop()


def imageOpen():
    global filePath
    filePath = tk.filedialog.askopenfilename()
    fp = open(filePath,'rb')
    global img
    img = Image.open(fp).convert("1",dither=Image.NONE)
    printImageToScreen(img)
    imageProcess()



def imageProcess():
    global img, nCol, nRow
    nCol, nRow = img.size

    colorMap = img.load()

    global framedImage
    framedImage = Image.new('RGB', ((nCol+2), (nRow+2)), color='black').convert('1', dither=Image.NONE)

    for r in range(1,nRow+1):
        for c in range(1,nCol+1):
            framedImage.putpixel((c,r), colorMap[c-1,r-1])

    global binaryImage
    binaryImage = [[0 for x in range(nCol)] for y in range(nRow)]

    global pixelMapAsString

    for r in range(nRow):
        for c in range(nCol):
            if colorMap[c,r] > 200:
                binaryImage[r][c] = 1
            else:
                binaryImage[r][c] = 0
            pixelMapAsString +=  str(binaryImage[r][c])
        pixelMapAsString += "\n"




def levialdi(framedImage):


    imgarray = np.array(framedImage.convert("1"))

    global nccLevialdi
    global iterationLevialdi
    nccLevialdi = 0
    iterationLevialdi = 0
    tempArray = deepcopy(imgarray)
    imgarray2 = deepcopy(imgarray)
    startTime = time.time()
    control = True
    while control:
        control = False

        for i in range(imgarray2.shape[0]):
            for j in range(imgarray2.shape[1]):
                if imgarray2[i][j] == 1:
                    if imgarray2[i - 1][j - 1] == 0 and imgarray2[i - 1][j] == 0 and imgarray2[i - 1][j + 1] == 0 and \
                            imgarray2[i][j + 1] == 0 and imgarray2[i + 1][j + 1] == 0 and imgarray2[i + 1][j] == 0 and \
                            imgarray2[i + 1][j - 1] == 0 and imgarray2[i][j - 1] == 0:
                        tempArray[i][j] = 0
                        nccLevialdi +=1
                        control = True
                    if imgarray2[i][j - 1] == 0 and imgarray2[i + 1][j - 1] == 0 and imgarray2[i + 1][j] == 0:
                        tempArray[i][j] = 0
                        control = True
                if imgarray2[i][j] == 0:
                    if imgarray2[i][j - 1] == 1 and imgarray2[i + 1][j] == 1:
                        tempArray[i][j] = 1
                        control = True

        imgarray2 = deepcopy(tempArray)
        imgarray2 = imgarray2*1
        iterations= ""
        for k in range(imgarray2.shape[0]):
            for l in range(imgarray2.shape[1]):
                iterations += str(imgarray2[k][l])
            iterations += "\n"


        root.LevialdiCanvas.delete("levid")
        root.LevialdiCanvas.create_text(160,325,font=("Arial", 3),text=iterations, tag="levid")
        root.LevialdiCanvas.update()
        if control:
            iterationLevialdi+=1

    global LevialdiCanvas


    root.itercounter.configure(text=iterationLevialdi)
    root.ncccounter.configure(text=nccLevialdi)

    root.Binary.insert(tk.INSERT,pixelMapAsString)





def printImageToScreen(img):
    render = ImageTk.PhotoImage(img)
    img = Label(root, image=render)
    img.image = render
    img.place(x=100, y=100)

if __name__ == '__main__':
    main()