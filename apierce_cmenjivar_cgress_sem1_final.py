'''apierce_cmenjivar_cgress_sem1_final.py
'''
import PIL
import matplotlib.pyplot as plt
import os.path   
directory = os.path.dirname(os.path.abspath(__file__))  
image1_file = os.path.join(directory, 'image1.jpg')
img1 = PIL.Image.open(image1_file)
fig, axes = plt.subplots(1, 1)
axes.imshow(img1, interpolation='none')
fig.show()

image2_file = os.path.join(directory, 'image2.png')
img2 = PIL.Image.open(image2_file)
img2_small = img2.resize((275, 165)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(img2)
axes2[1].imshow(img2_small)
fig2.show()

img1.paste(img2_small, (293, 221))
fig3, axes3 = plt.subplots(1, 1)
axes3.imshow(img1, interpolation='none')

fig3.show()