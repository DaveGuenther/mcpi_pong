import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong import utility
from pong.render import Screen
from pong.render import Clipper
from pong.render import PixelArray

class TestClipper(unittest.TestCase):

    def test_clip_sprite_with_single_edge_noclip(self):
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
        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,my_sprite_array.T))

        screen_edge=(0,0)
        screen_edge_normal_vec=(0,1) # top

        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,my_sprite_array.T))

        screen_edge=(this_screen.getWidth(),0)
        screen_edge_normal_vec=(-1,0) # right

        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,my_sprite_array.T))

        screen_edge=(0,this_screen.getHeight())
        screen_edge_normal_vec=(0,-1) # bottom

        clipped_sprite,sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,my_sprite_array.T))



    def test_clip_sprite_with_single_edge_top_left(self):
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


        #self.assertIs(my_clipper.my_screen, this_screen, f"Screen objects do not occupy same memory address")

        # Create top_left assert val
        top_left_assert=np.array([
            [5,6],
            [8,10]
        ])

        screen_edge=(0,0)
        screen_edge_normal_vec=(1,0) # left
        sprite_start_pos=(-1,-1)
        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        screen_edge=(0,0)
        screen_edge_normal_vec=(0,1) # top

        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,top_left_assert.T))



    def test_clip_sprite_with_single_edge_bottom_right(self):
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


        #self.assertIs(my_clipper.my_screen, this_screen, f"Screen objects do not occupy same memory address")

        # Create top_left assert val
        bot_right_assert=np.array([
            [1,2],
            [4,5]
        ])

        screen_edge=(this_screen.getWidth(),0)
        screen_edge_normal_vec=(-1,0) # right
        sprite_start_pos=(3,4)
        clipped_sprite, sprite_start_pos= my_clipper.clip_sprite_with_single_edge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        screen_edge=(0,this_screen.getHeight())
        screen_edge_normal_vec=(0,-1) # bottom
        clipped_sprite, sprite_start_pos = my_clipper.clip_sprite_with_single_edge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.data,bot_right_assert.T), f"clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(3,4),f"Sprite Start Position is incorrect")

if __name__ == '__main__':
    unittest.main()