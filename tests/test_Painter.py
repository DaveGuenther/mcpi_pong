import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong import utility
from pong.render import Painter


class TestPainter(unittest.TestCase):
    def test_init(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,8,12)
        this_painter = Painter

        self.assertIs(my_screen.mc_connection, mc, f"mcpi objects do not occupy same memory address")
       


    def test_paintSprite(self):
        pass


    def test_fillCanvas(self):
        pass


if __name__ == '__main__':
    unittest.main()