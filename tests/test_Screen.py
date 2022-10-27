import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong import utility
from pong.render import Screen

class TestScreen(unittest.TestCase):
    def test_create_screen(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)
        #self.assertTrue(my_screen.__front_virtual_page.getHeight()==32, f"current screen array heights do not match")
        #self.assertTrue(my_screen.__front_virtual_page.getWidth()==16, f"current screen array widths do not match")
        #self.assertTrue(my_screen.__back_virtual_page.getHeight()==32, f"new screen array heights do not match")
        #self.assertTrue(my_screen.__back_virtual_page.getWidth()==16, f"new screen array widths do not match")

        self.assertIs(my_screen.mc_connection, mc, f"mcpi objects do not occupy same memory address")


if __name__ == '__main__':
    unittest.main()