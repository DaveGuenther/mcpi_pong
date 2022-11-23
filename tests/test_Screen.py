import unittest
import numpy as np
import pickle
from .fake_minecraft import Minecraft
from pong import utility
from pong.render import Screen
from pong.render import PixelArray
from pong.vector import MCVector


class TestScreen(unittest.TestCase):
    def test_create_screen(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)

        self.assertIs(my_screen.mc_connection, mc, f"mcpi objects do not occupy same memory address")

    def test_fillActivePage(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,16,32)

        assert_val=np.array(
            [
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            ]
        )
        my_screen.fill(1)
        data = my_screen.getBackVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData(),assert_val))

        assert_val=np.array(
            [
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9],
                [9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]
            ]
        )

        my_screen.fill(9)
        data = my_screen.getBackVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData(),assert_val))
        


    def test_drawObject(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,8,12)        


        sprite=PixelArray(np.array(
            [
                [3,4,5],
                [6,7,8],
                [9,10,11],
                [12,13,14]
            ]
        ))

        sprite_start_pos=(2,1)

        assert_val=np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 4, 5, 0, 0, 0],
                [0, 0, 6, 7, 8, 0, 0, 0],
                [0, 0, 9,10,11, 0, 0, 0],
                [0, 0,12,13,14, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        )
        my_screen.drawObject(sprite,sprite_start_pos)
        data = my_screen.getBackVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData().T,assert_val))


    def test_flipVirtualPage(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,8,12)        


        sprite=PixelArray(np.array(
            [
                [3,4,5],
                [6,7,8],
                [9,10,11],
                [12,13,14]
            ]
        ))

        sprite_start_pos=(2,1)

        assert_val=np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        )
        my_screen.drawObject(sprite,sprite_start_pos)
        my_screen.flipVirtualPage()
        data = my_screen.getBackVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData().T,assert_val))

        assert_val=np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 3, 4, 5, 0, 0, 0],
                [0, 0, 6, 7, 8, 0, 0, 0],
                [0, 0, 9,10,11, 0, 0, 0],
                [0, 0,12,13,14, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ]
        )

        data = my_screen.getFrontVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData().T,assert_val))


    def test_removeUnchangedBlocksFromRedraw(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen([mc],top_left_screen_coord,8,12)        


        sprite=PixelArray(np.array(
            [
                [3,4,5],
                [6,7,8],
                [9,10,11],
                [12,13,14]
            ]
        ))

        sprite_start_pos=(2,1)

        assert_val=np.array(
            [
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 3, 4, 5, 9, 9, 9],
                [9, 9, 6, 7, 8, 9, 9, 9],
                [9, 9, 9,10,11, 9, 9, 9],
                [9, 9,12,13,14, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9, 9, 9, 9]
            ]
        )
        my_screen.drawObject(sprite,sprite_start_pos)
        my_screen.removeUnchangedBlocksFromRedraw()
        data = my_screen.getBackVirtualPage()
        self.assertIsNone(np.testing.assert_array_equal(data.getData().T,assert_val))



if __name__ == '__main__':
    unittest.main()