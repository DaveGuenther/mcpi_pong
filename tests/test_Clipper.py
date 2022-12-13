import unittest
import numpy as np
import pickle

from pong.vector import MCVector
import os
if int(os.environ['MC_Live_Connection'])==1:
    from mcpi.minecraft import Minecraft
    print("importing real MC")
else:
    from .mock_minecraft import Minecraft
    print("importing fame MC")
from pong import utility
from pong.render import Screen
from pong.render import Clipper
from pong.render import PixelArray

class TestClipper(unittest.TestCase):

    def test_clipSpriteWithSingleEdge_noclip(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) #pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        
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
        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),my_sprite_array.T))

        screen_edge=(0,0)
        screen_edge_normal_vec=(0,1) # top

        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),my_sprite_array.T))

        screen_edge=(this_screen.getWidth(),0)
        screen_edge_normal_vec=(-1,0) # right

        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),my_sprite_array.T))

        screen_edge=(0,this_screen.getHeight())
        screen_edge_normal_vec=(0,-1) # bottom

        clipped_sprite,sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),my_sprite_array.T))
        mc.conn.socket.close()



    def test_clipSpriteWithSingleEdge_top_left(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958)
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
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
        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        screen_edge=(0,0)
        screen_edge_normal_vec=(0,1) # top

        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),top_left_assert.T))
        mc.conn.socket.close()



    def test_clipSpriteWithSingleEdge_bottom_right(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) #pixel Display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_screen = Screen([mc],top_left_screen_coord,4,5)
        my_clipper = Clipper([this_screen])
        
        # Create Sprite
        my_sprite_array=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10]
        ])

        this_sprite = PixelArray(my_sprite_array)

        # Create bottom_right assert val
        bot_right_assert=np.array([
            [1,2],
            [4,5]
        ])

        screen_edge=(this_screen.getWidth(),0)
        screen_edge_normal_vec=(-1,0) # right
        sprite_start_pos=(3,4)
        clipped_sprite, sprite_start_pos= my_clipper.clipSpriteWithSingleEdge(this_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        screen_edge=(0,this_screen.getHeight())
        screen_edge_normal_vec=(0,-1) # bottom
        clipped_sprite, sprite_start_pos = my_clipper.clipSpriteWithSingleEdge(clipped_sprite, sprite_start_pos, screen_edge, screen_edge_normal_vec)

        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),bot_right_assert.T), f"clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(3,4),f"Sprite Start Position is incorrect")
        mc.conn.socket.close()

    def test_clip_sprite_with_all_edges(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display)
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_screen = Screen([mc],top_left_screen_coord,8,12)
        my_clipper = Clipper([this_screen])
        
        # Create Sprite
        my_sprite_array=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10],
            [11,12,13]
        ])

        this_sprite = PixelArray(my_sprite_array)

        # assert val 1
        assert_val=np.array([
            [6],
            [10],
            [13]
        ])

        sprite_start_pos=(-2,-1)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 1: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,0),f"Assert 1: Sprite Start Position is incorrect")

        # assert val 2
        assert_val=np.array([
            [4,5,6],
            [7,8,10],
            [11,12,13]
        ])
        sprite_start_pos=(3,-1)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 2: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(3,0),f"Assert 2: Sprite Start Position is incorrect")

        # assert val 3
        assert_val=np.array([])
        sprite_start_pos=(-5,4)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 3: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,0),f"Assert 3: Sprite Start Position is incorrect")


        # assert val 4
        assert_val=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10],
            [11,12,13]
        ])
        sprite_start_pos=(1,3)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 4: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(1,3),f"Assert 4: Sprite Start Position is incorrect")


        # assert val 5
        assert_val=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10],
            [11,12,13]
        ])
        sprite_start_pos=(5,3)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 5: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(5,3),f"Assert 5: Sprite Start Position is incorrect")

        # assert val 6
        assert_val=np.array([])
        sprite_start_pos=(10,3)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 6: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,3),f"Assert 6: Sprite Start Position is incorrect")

        # assert val 7
        assert_val=np.array([
            [1,2,3],
            [4,5,6],
            [7,8,10],
            [11,12,13]
        ])
        sprite_start_pos=(0,7)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 7: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,7),f"Assert 7: Sprite Start Position is incorrect")

        # assert val 8
        assert_val=np.array([
            [1,2],
            [4,5],
            [7,8]
        ])
        sprite_start_pos=(6,9)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 8: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(6,9),f"Assert 8: Sprite Start Position is incorrect")


        # assert val 9
        assert_val=np.array([
            [3]
        ])
        sprite_start_pos=(-2,11)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 9: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,11),f"Assert 9: Sprite Start Position is incorrect")

        # assert val 10
        assert_val=np.array([])
        sprite_start_pos=(3,12)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 10: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,0),f"Assert 10: Sprite Start Position is incorrect")

        # assert val 11
        assert_val=np.array([])
        sprite_start_pos=(2,16)
        clipped_sprite, sprite_start_pos = my_clipper.clipObjectWithScreenEdges(this_sprite, sprite_start_pos)
        self.assertIsNone(np.testing.assert_array_equal(clipped_sprite.getData(),assert_val.T), f"Assert 11: clipped sprite does not match")
        self.assertEqual(sprite_start_pos,(0,0),f"Assert 11: Sprite Start Position is incorrect")
        mc.conn.socket.close()



if __name__ == '__main__':
    unittest.main()