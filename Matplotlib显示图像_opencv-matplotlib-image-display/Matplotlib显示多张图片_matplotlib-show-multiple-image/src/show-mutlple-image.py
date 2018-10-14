import cv2
from matplotlib import pyplot as plt
img = cv2.imread('cat.jpg')

b, g, r = cv2.split(img)


plt.subplot(2, 2, 1)
plt.title('origin')
plt.imshow(img[:,:,::-1])

plt.subplot(2, 2, 2)
plt.title('blue channel')
plt.imshow(b, cmap='Blues')

plt.subplot(2, 2, 3)
plt.title('green channel')
plt.imshow(g, cmap='Greens')

plt.subplot(2, 2, 4)
plt.title('red channel')
plt.imshow(r, cmap='Reds')


plt.show()

