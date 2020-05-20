from PIL import *
from PIL import Image
import numpy as np
import copy

def main():
    print("hi")
    img = readPILimg()
    arr = img2array(img)
    ONE = 100
    bim = binary_image(100, 100, ONE)
    new_img = NP2PIL(bim)

    ncol, nrow = img.size
    for i in range(nrow):
        for j in range(ncol):
            if arr[i, j] > 149:
                arr[i, j] = 1
            else:
                arr[i, j] = 0
            print(arr[i, j], end="")
        print("")
    print("\n")

    levialdi(arr, ONE)

def readPILimg():
    img = Image.open("C:/Users/themr/Desktop/sample_images/NCC4_ITER128.png", 'r')
    img_gray = color2gray(img)
    img_gray = img_gray.resize((256,256))
    return img_gray


def color2gray(img):
    img_gray = img.convert('L')
    return img_gray

def img2array(img):
    nrows = img.size[0]
    ncols = img.size[1]
    print("nrows, ncols : ", nrows,ncols)
    imgarray = np.array(img.convert("L"))
    return imgarray

def binary_image(nrow,ncol,Value):
#creates a binary image with size nrow x ncol with pixel values Value
    x, y = np.indices((nrow, ncol))
    mask_lines = np.zeros(shape=(nrow,ncol))

    x0, y0, r0 = 30, 30, 10
    x1, y1, r1 = 70, 30, 10


    for i in range (50, 70):
        mask_lines[i][i] = 1
        mask_lines[i][i + 1] = 1
        mask_lines[i][i + 2] = 1
        mask_lines[i][i + 3] = 1
        mask_lines[i][i + 6] = 1

    # mask_circle1 = np.abs((x - x0) ** 2 + (y - y0) ** 2 - r0 ** 2 ) <= 5
    mask_square1 = np.fmax(np.absolute( x - x1), np.absolute( y - y1)) <= r1
    # mask_square2 = np.fmax(np.absolute( x - x2), np.absolute( y - y2)) <= r2
    # mask_square3 = np.fmax(np.absolute( x - x3), np.absolute( y - y3)) <= r3
    # mask_square4 =  np.fmax(np.absolute( x - x4), np.absolute( y - y4)) <= r4
    # imge = np.logical_or ( np.logical_or(mask_lines, mask_circle1), mask_square1) * Value
    imge = np.logical_or(mask_lines, mask_square1) * Value

    return imge

def NP2PIL(im): #converts numpy array to a PIL image
    print("size of arr: ",im.shape)
    img = Image.fromarray(np.uint8(im))
    return img


def levialdi(arr, ONE):

        w, h = 100, 100;
        arr2 =
        arr2 = copy.deepcopy(arr)
        while (whileloop(arr) == True):
            for i in range(ONE - 1, 0, -1):
                for j in range(0, ONE - 1):
                    arr[i, j] = arr2[i, j]
                    if arr[i, j] == 1:
                        if arr[i, j - 1] == 0 and arr[i + 1, j - 1] == 0 and arr[i + 1, j] == 0:
                            arr[i, j] = 0
                        elif arr[i, j - 1] == 0 and arr[i + 1, j - 1] == 0 and arr[i + 1, j] == 0 and arr[i - 1, j - 1] == 0 and \
                            arr[i - 1, j] == 0 and arr[i - 1, j + 1] == 0 and arr[i, j + 1] == 0 and arr[i + 1, j + 1] == 0:
                            arr[i, j] = 0
                    elif arr[i, j] == 0:
                        if arr[i, j - 1] == 1 and arr[i + 1, j] == 1:
                            arr[i, j] = 1

        print(arr)

def whileloop(arr):
    abc = True
    for i in range (100):
        for j in range (100):
            if arr[i, j] == [0, 1]:
                abc=True
            elif arr[i, j] == [1, 0]:
                abc=True
                if arr[i, j] == [1, 1]:
                    abc=True
            else:
                abc=False





if __name__=='__main__':
    main()

