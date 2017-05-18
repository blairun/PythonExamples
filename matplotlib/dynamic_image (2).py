"""
=================
An animated image
=================

This example demonstrates how to animate an image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 50))

def f(x, y):
    return np.sin(x) + np.cos(y)

x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)

# im = plt.imshow(f(x, y), animated=True)
img = plt.imread("bulb.jpg")
im2 = plt.imread("download.jpg")

img_p = plt.imshow(img, extent=(0,1,0,1))
im2_p = plt.imshow(im2, extent=(0, 50, 0, 50))


# initialization function: plot the background of each frame
def init():
    plt.imshow(im2, extent=(0,50,0,50))
    #im.set_data(np.random.random((5, 5)))
    # return img


def updatefig(i):
    #global x, y
    i += 1
    #plt.imshow(im2, extent=(0, 50, 0, 50))
    #data =
    #img_p.set_data(data)
    fig.canvas.draw()
    plt.imshow(img, extent=(i, i+1, i, i+1))

    #x += np.pi / 15.
    #y += np.pi / 20.
    #im.set_array(f(x, y))
    #x += 1
    #img.resize(1.1*x)
    #return im,
    #return img

ani = animation.FuncAnimation(fig, updatefig, init_func=init, interval=50) #, blit=True)
#ani = animation.FuncAnimation(fig, updatefig, 40, interval=100, blit=False)
#plt.imshow(img, extent=(0,1,0,1))
plt.show()
