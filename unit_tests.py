import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
#from tests.fake_minecraft import Minecraft
from pong.render import PixelArray
from pong.render import Renderer
from pong.vector import MCVector
from mcpi import vec3
import time


my_file= open( "server.pkl", "rb" ) 
server_ip, server_port = pickle.load(my_file)
my_file.close()
mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958)
this_painter = Renderer([mc], top_left_screen_coord, 16,32)

this_painter.putPixel((3,4), 6)
ret_val = this_painter.getColorAt((3,4),1)
this_painter.flipVirtualPage()

my_sprite = PixelArray(np.array(
    [
        [16,16,16,16,16],
        [16, 1,16, 1,16],
        [16,16,10,16,16],
        [16, 3,16, 3,16],
        [16,16, 3,16,16]
    ]
))

this_painter.paintSprite(my_sprite, (2,2))
ret_val = this_painter.getColorAt((4,7),1)
this_painter.flipVirtualPage()
this_painter.fillCanvas(0)
this_painter.flipVirtualPage()

print("Hello Pong!")

from pong import input
from pong.vector import MCVector

mc = Minecraft.create(server_ip,server_port)
this_painter = Renderer([mc], top_left_screen_coord, 16,32,type='cart')

# define p1 paddle sprite
p1_sprite = PixelArray(np.array(
    [
        [16,16,16,16]
    ]))

# p1 controller
p1_input_start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39955))
p1_input_end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39962))
p1_controller = input.RangeInput([mc],start_coord=p1_input_start_coord, end_coord=p1_input_end_coord)


# define p1 paddle sprite
p2_sprite = PixelArray(np.array(
    [
        [16,16,16,16]
    ]))
p1_pos = np.array([0,-14])
p2_pos = np.array([0,14])

# p2 controller
p2_input_start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39969))
p2_input_end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 83, 39976))
p2_controller = input.RangeInput([mc],start_coord=p2_input_start_coord, end_coord=p2_input_end_coord)

while 1:
    #Scan MC input
    p1_controller.scanInput()
    p2_controller.scanInput()
    
    #adjust ships based on input
    p1_pos[0] = (this_painter.getScreenWidth()-p1_sprite.getWidth())*p1_controller.getInputValue()-8  # doing screen_width(16)-ship_length (4) makes it so that ship can easily move from edge to edge
    p2_pos[0] = (this_painter.getScreenWidth()-p2_sprite.getWidth())*p2_controller.getInputValue()-8
    print("P1:",p1_controller.getInputValue(), p1_pos[0],"   P2:",p2_controller.getInputValue(),p2_pos[0])
    
    #clear canvas
    this_painter.fillCanvas(0)
    
    #place sprites
    this_painter.paintSprite(p1_sprite, p1_pos)
    this_painter.paintSprite(p2_sprite, p2_pos)
    
    #show screen
    this_painter.flipVirtualPage()
    #time.sleep(.05)
print("Hello")

