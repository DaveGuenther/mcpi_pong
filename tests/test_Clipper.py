import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong.render import Screen
from pong.render import Clipper
from pong.render import PixelArray

class TestClipper(unittest.TestCase):
    def test_create_clipper(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_screen = Screen([mc],top_left_screen_coord,16,32)
        my_clipper = Clipper([this_screen])
        
        self.assertIs(my_clipper.my_screen, this_screen, f"mcpi objects do not occupy same memory address")


if __name__ == '__main__':
    unittest.main()