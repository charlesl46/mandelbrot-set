#native libraries
import math
import random
import time
import colorsys
import os

#downloaded libraries
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw
from tqdm import tqdm

#constants
MAX_ITER = 25
RE_START = -2
RE_END = 2
IM_START = -2
IM_END = 2




def init(resolution):
    resolution = int(resolution)
    width = resolution
    height = width
    im = Image.new('RGB',(width,height),(0,0,0))
    draw = ImageDraw.Draw(im)
    return (height,width),im,draw


#function to get at which iteration a 'z' sequence diverges
#it also gives its last value, to be used later to colour the center of the set. 
def number_iterations(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1
    #norm of the last complex value
    last_value = (np.real(z)**2+np.imag(z)**2)**(1/2)
    return n,last_value


#this lets you choose between the two color systems
def get_color_system(color_system,rd):

    choice = color_system
    #this gives them all the same weight, maximal weight : 1
    red_int = 1
    green_int = 1
    blue_int = 1
    red_out = 1
    green_out = 1
    blue_out = 1
    #this gives random weights to the red green and blue components of the code
    randoms_int = []
    randoms_out = []
    if rd:
        red_int = random.random()
        green_int = random.random()
        blue_int = random.random()
        red_out = random.random()
        green_out = random.random()
        blue_out = random.random()
        
    randoms_int.append(red_int)
    randoms_int.append(green_int)
    randoms_int.append(blue_int)
    randoms_out.append(red_out)
    randoms_out.append(green_out)
    randoms_out.append(blue_out)

    return choice,randoms_int,randoms_out



#this converts the coordinates from our mathematic system to the system of the PIL window
def convert_coor(x,y,dimensions):
    WIDTH,HEIGHT = dimensions
    return complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))

#this adapts the plot in function of the color system you chose before
def color_system_maker(choice,m,randoms_out,randoms_int,last_value,max):
    if choice == 'hsv':
        #out
        if m < MAX_ITER:
            hue = m / MAX_ITER
            saturation = 1
            value = 1
            couleur = colorsys.hsv_to_rgb(hue,saturation,value)
            couleur = (couleur[0]*randoms_out[0]*255,couleur[1]*randoms_out[1]*255,couleur[2]*randoms_out[2]*255)
        else: #in
            hue = last_value/max
            saturation = 1
            value = 1
            couleur = colorsys.hsv_to_rgb(hue,saturation,value)
            couleur = (couleur[0]*randoms_int[0]*255,couleur[1]*randoms_int[1]*255,couleur[2]*randoms_int[2]*255)

        color = (int(couleur[0]),int(couleur[1]),int(couleur[2]))
        return color
    elif choice == 'rgb':
        #out 
        if m < MAX_ITER:
            ratio = 255 - int(m * 255 / MAX_ITER)
            color = (int(randoms_out[0]*ratio),int(randoms_out[1]*ratio),int(randoms_out[2]*ratio))
        #in
        else:
            ratio = (last_value/1.5) * 255
            color = (int(randoms_int[0]*ratio),int(randoms_int[1]*ratio),int(randoms_int[2]*ratio))
        return color
    pass

def plot(resolution,color_system,random):
    dimensions,im,draw = init(resolution)
    WIDTH,HEIGHT = dimensions
    choice,randoms_int,randoms_out = get_color_system(color_system,random)
    beginning = time.time()
    nb_values = WIDTH * HEIGHT
    max = 0
    for x in tqdm(range(0, WIDTH)):
        for y in range(0, HEIGHT):
            c = convert_coor(x,y,dimensions)
            last_iteration,last_value = number_iterations(c)
            if last_value > max:
                max = last_value
            color = color_system_maker(color_system,last_iteration,randoms_out,randoms_int,last_value,max)
            #to plot the point
            draw.point([x, y], color)
    end = time.time()
    print(f'{nb_values} plots in {round(end-beginning,3)} seconds')

    return im,dimensions

def save(im,dimensions,folder):
    WIDTH,HEIGHT = dimensions
    path = folder
    filesInDir = os.listdir(path)
    print(filesInDir)
    nb = 0
    name = (f'output{nb} {WIDTH} x {HEIGHT}.png')
    while name in filesInDir:
        nb += 1
        name = (f'output{nb} {WIDTH} x {HEIGHT}.png')
    name = (f'output{nb} {WIDTH} x {HEIGHT}.png')
    print(f'name = {name}')

    try:
        im.convert('RGB').save(path+'/'+name, 'PNG')
        print(f'Successfully saved as {name} in {path}')
    except FileNotFoundError :
        print('Saving failed')


#main
def main(resolution,folder,color_system,random):
    im, dimensions = plot(resolution,color_system,random)
    save(im,dimensions,folder)










