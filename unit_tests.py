import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import PixelArray
from pong.render import Renderer
from mcpi import vec3


my_file= open( "server.pkl", "rb" ) 
server_ip, server_port = pickle.load(my_file)
my_file.close()
mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
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

print("Hello Minecraft!")

from pong import input
from pong.vector import MCVector

my_controller = input.TactileInput([mc],MCVector.from_MCWorld_Vec(vec3.Vec3(39522, 78, 39958)), MCVector.from_MCWorld_Vec(vec3.Vec3(39522, 79, 39954)))
print("Hello")