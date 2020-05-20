import tkinter as tk
from tkinter.filedialog import *
from PIL import Image, ImageTk
from copy import copy, deepcopy


root = tk.Tk()
root.geometry("1024x1024")
root.title("Emre Arslan Project")
root.configure(bg='salmon')

background_image=PhotoImage('C:/Users/themr/Desktop/sample_images/NCC4_ITER15.png.png')
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

types = (("pngs", "*.png"), ("bmp", ".bmp"))
path = askopenfilename(parent=root, filetypes=types)

fp = open(path, "rb")
img = Image.open(fp)
img = img.convert('1')



def readPILimg(): #read image file using PIL
    pix = img.load()
    img.show()
    return pix

pix = img.load()
pix[0,0]
#pix2 = deepcopy(pix)
ncol, nrow = img.size

def PIL2np(pix): #converts image in PIL format to a numpy array
    nrows = img.size[0]
    ncols = img.size[1]
    print("nrows, ncols : ", nrows,ncols)
    pix2 = np.array(img.convert("L"))
    return pix

ncc=0
iter=0

for r in range(nrow):
    for c in range(ncol):
        if pix[c,r]>200:
            print(1, end="")
        else:
            print(pix[c,r], end="")
    print("")


    def levialdi(pix, ONE):

        w, h = 100, 100;
        pix2 = [[0 for x in range(w)] for y in range(h)]
        pix2 = copy.deepcopy(pix)
        while (whileloop(pix) == True):
            for i in range(ONE - 1, 0, -1):
                for j in range(0, ONE - 1):

                    pix[i, j] = pix2[i, j]
                    if pix[i, j] == 1:
                        if pix[i, j - 1] == 0 and pix[i + 1, j - 1] == 0 and pix[i + 1, j] == 0:
                            pix[i, j] = 0

                        elif pix[i, j - 1] == 0 and pix[i + 1, j - 1] == 0 and pix[i + 1, j] == 0 and pix[
                            i - 1, j - 1] == 0 and \
                                pix[i - 1, j] == 0 and pix[i - 1, j + 1] == 0 and pix[i, j + 1] == 0 and pix[
                            i + 1, j + 1] == 0:
                            pix[i, j] = 0

                    elif pix[i, j] == 0:
                        if pix[i, j - 1] == 1 and pix[i + 1, j] == 1:
                            pix[i, j] = 1
            imgZ = Image.fromarray(pix * 255, 'L')
            imgZ.show()

def whileloop(pix):
    abc = True
    for i in range(100):
        for j in range(100):
            if (pix[i, j] == 1):
                abc = False
                return abc
            else:
                abc = True
                return abc
    return abc


print("")
print(ncol, nrow)

root.mainloop()