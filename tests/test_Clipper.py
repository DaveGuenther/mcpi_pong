import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong import utility
from pong.render import Screen
from pong.render import Clipper
from pong.render import PixelArray

class TestClipper(unittest.TestCase):

    def test_clip_sprite_with_single_edge(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_screen = Screen([mc],top_left_screen_coord,4,5)
        my_clipper = Clipper([this_screen])
        
        # Create Sprite
        my_sprite_array=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10]
        ])

        this_sprite = PixelArray(my_sprite_array)

        screen_edge=(0,0)
        screen_edge_normal_vec=(1,0) # left
        sprite_start_pos=(1,1)
        clipped_sprite = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,my_sprite_array.T))

        #self.assertIs(my_clipper.my_screen, this_screen, f"Screen objects do not occupy same memory address")


if __name__ == '__main__':
    unittest.main()