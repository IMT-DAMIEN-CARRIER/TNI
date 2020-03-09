# import Pillow
"""
import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread("lena_gray.")

if img.dtype == np.float32: # Si le résultat n'est pas un tableau d'entiers
    img = (img * 255).astype(np.uint8)
image2 = np.copy(img)

print(image2.shape)"""

def openFile():
    f = open(".\\lena_gray.raw")
    print(f)
    texte = f.read()
    print(texte)
    f.close()
openFile()