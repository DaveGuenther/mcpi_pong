import unittest
import numpy as np
import pickle
from pong import utility
from mcpi.minecraft import Minecraft
from pong.render import Color
from pong.render import Screen
from pong.render import PixelArray
from pong.render import Clipper
from pong.render import Painter


my_file= open( "server.pkl", "rb" ) 
server_ip, server_port = pickle.load(my_file)
my_file.close()
mc = Minecraft.create(server_ip,server_port)
top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
this_painter = Painter([mc], top_left_screen_coord, 8, 12)

this_painter.fillCanvas(7)
ret_val = this_painter.getColorAt((3,4),1)        



print("Hello Minecraft!")