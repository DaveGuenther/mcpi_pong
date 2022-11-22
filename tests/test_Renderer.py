import unittest
import numpy as np
import pickle
from mcpi.minecraft import Minecraft
from pong import utility
from pong.render import Renderer
from pong.render import PixelArray
from pong.vector import MCVector


class TestRenderer(unittest.TestCase):
    def test_init(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_painter = Renderer([mc], top_left_screen_coord, 8, 12)

        self.assertIsInstance(this_painter, Renderer, f"Painter class failed to initialize")

    def test_paintSprite_getPixel_flipVirtualPage(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        #top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958)
        this_painter = Renderer([mc], top_left_screen_coord, 8,12)

        my_sprite = PixelArray(np.array(
            [
                [16,16,16,16,16],
                [16, 1,16, 1,16],
                [16,16,10,16,16],
                [16, 3,16, 3,16],
                [16,16, 3,16,16]
            ]
        ))

        this_painter.paintSprite(my_sprite, (2,2))
        ret_val = this_painter.getColorAt((4,6),1)
        this_painter.flipVirtualPage()
        ret_val = this_painter.getColorAt((4,6))

        self.assertEqual(ret_val, 3,f"Pixel color values do not match")

    def test_putPixel_getPixel(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_painter = Renderer([mc], top_left_screen_coord, 8,12)

        this_painter.putPixel((3,4), 6)
        ret_val = this_painter.getColorAt((3,4),1)

        self.assertEqual(ret_val, 6,f"Pixel color values do not match")

    def test_fillCanvas(self):
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        this_painter = Renderer([mc], top_left_screen_coord, 8, 12)

        this_painter.fillCanvas(7)
        ret_val = this_painter.getColorAt((3,4),1)        
        self.assertEqual(ret_val, 7)

if __name__ == '__main__':
    unittest.main()