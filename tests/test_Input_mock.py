# The difference between these unit tests and the ones in test_Input.py is that these REQUIRE invoking the mock_minecraft 
# class in order to properly test the edge cases of the input class, as it would otherwise be imposible to place a player
# at all possible locations in the real world

import unittest
from pong import utility
from pong.vector import MCVector
from mcpi import vec3
from pong import input
import os
from .mock_minecraft import Minecraft


import pickle

class TestInput(unittest.TestCase):
    def testRangeInputInstance(self):
        """
        Tests for RangeInput defining a line of blocks and testing for a player block at the beginning, middle, and end of that line to check linear interpolation values (0-1)
        """

        #player_id = 0  #just need some integer here
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39962))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        
        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39955)) # player at start of platform
        my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 0.0)

        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39962)) # player at end of platform
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 1.0)

        mc.entity.player_pos=MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39958)) # player somewhere near middle of controller
        my_controller.scanInput()
        lerp_val=my_controller.getInputValue()
        self.assertAlmostEqual(lerp_val, 0.42857142)
                



if __name__ == '__main__':
    unittest.main()