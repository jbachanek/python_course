import matplotlib.pyplot as plt
import matplotlib.image as img
import matplotlib.colors as clr
import os
from zadanie3 import reduce
import numpy as np

img_source="/home/kuba/PycharmProjects/python_course/resources/lab2"
img_file = "meil.png"
input_img = img.imread(img_source+os.sep+img_file)

nsize = 20

#wykorzystujac zad. 3 - wyciagam kanaly i skaluje wartosci
R = reduce(input_img[:, :, 0], (nsize, nsize))
G = reduce(input_img[:, :, 1], (nsize, nsize))
B = reduce(input_img[:, :, 2], (nsize, nsize))

#watosci przypisuje nowej tablicy
output_img = np.zeros((nsize, nsize, 3))
output_img[:, :, 0] = R
output_img[:, :, 1] = G
output_img[:, :, 2] = B

#kopijemy wynikowy i przerabiamy na hsv, nasycenie value
output_img_hsv = clr.rgb_to_hsv(output_img)
output_img_hsv[:, :, 1] = 0

output_hsv = np.copy(output_img_hsv)

_, (img_1, img_2, img_3) = plt.subplots(1, 3)
img_1.imshow(input_img)
img_2.imshow(output_img)
img_3.imshow(output_hsv)
plt.show()

dark = np.zeros((nsize,nsize), dtype = bool)
grey = np.copy(dark)

for i in range(nsize):
    for j in range(nsize):
        if(output_img_hsv[i, j, 2]<0.3):
            output_hsv[i, j, 2] = 0
            dark[i, j] = True
        elif(output_img_hsv[i, j, 2] < 0.6):
            output_hsv[i, j, 2] = 0.3
            grey[i, j] = True
        else:
            output_hsv[i, j, 2] = 1

#do tekstu
with open("output.txt", "w") as out:
    for i, j in zip(dark, grey):
        linia = np.array(["  "]*nsize)
        linia[i] = "||"
        linia[j] = "- "
        out.write("".join(linia))
        out.write("\n")


_, (img_1, img_2, img_3) = plt.subplots(1, 3)
img_1.imshow(input_img)
img_2.imshow(output_img)
img_3.imshow(output_hsv)
plt.show()