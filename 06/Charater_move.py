import os
import math
from pico2d import *

os.chdir('d:/2DGP/2017180027_Drill/Lecture04_2D_Rendering')

open_canvas()

grass = load_image('grass.png')
charater = load_image('character.png')

pattern = 0

def draw_charater(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    charater.draw_now(x, y)

def move_square():
    x = 400
    y = 90
    while (x < 800):
        draw_charater(x,y)
        x += 2

    while (y < 600):
        draw_charater(x,y)
        y += 2

    while (x > 0):
        draw_charater(x,y)
        x -= 2

    while (y > 90):
        draw_charater(x,y)
        y -= 2

    while (x < 400):
        draw_charater(x,y)
        x += 2
    
def move_circle():
    x = 400
    y = 90
    r = (600 - 90)/2

    for n in range(270,360+1):
        x = 400 + math.cos(n/360 * 2 * math.pi) * r
        y = 90  + r + math.sin(n/360 * 2 * math.pi) * r
        draw_charater(x,y)
        
    for n in range(0,270 + 1):
        x = 400 + math.cos(n/360 * 2 * math.pi) * r
        y = 90  + r + math.sin(n/360 * 2 * math.pi) * r
        draw_charater(x,y)
    
while(True) :
    if(pattern%2 == 0):
        move_square()
    else:
        move_circle()

    pattern+=1

close_canvas()
