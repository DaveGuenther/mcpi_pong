import unittest
import numpy as np
import pickle
import os
if int(os.environ['MC_Live_Connection'])==1:
    from mcpi.minecraft import Minecraft
    print("importing real MC")
else:
    from .fake_minecraft import Minecraft
    print("importing fame MC")
from pong import utility
from pong.render import Screen
from pong.coordinate_tools import CoordinateTools
from pong.vector import MCVector


class TestCartesian_Converter(unittest.TestCase):
    def testInstance(self):
        
        # initialize test env
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)
        
        
        # invoke class instance
        my_coord_tools=CoordinateTools([my_screen])

        # assert unittest
        self.assertIsInstance(my_coord_tools, CoordinateTools)

    def testCartToScreen(self):
        
        # initialize test env
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)
        
        # invoke class instance
        my_coord_tools=CoordinateTools([my_screen])

        #perform test
        out_coords=my_coord_tools.cartToScreen(np.array([4,-2]))

        # assert unittest
        self.assertTrue((out_coords==np.array([10,14])).all())

    def testScreenToCart(self):
        
        # initialize test env
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)
        
        # invoke class instance
        my_coord_tools=CoordinateTools([my_screen])

        #perform test
        out_coords=my_coord_tools.screenToCart(np.array([10,14]))

        # assert unittest
        self.assertTrue((out_coords==np.array([4,-2])).all())


if __name__ == '__main__':
    unittest.main()