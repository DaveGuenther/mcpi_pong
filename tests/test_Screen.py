import unittest
import numpy as np
from mcpi.minecraft import Minecraft
from pong.render import Screen

class TestScreen(unittest.TestCase):
    def test_create_screen(self):
        server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
        mc = Minecraft.create(server_ip,server_port)
        top_left_screen_coord = utility.get_mcpi_vec_from_world_coords(39562, 106, 39958) # pixel display
        my_screen = Screen(mc,top_left_screen_coord)
        self.assert(np.testing.assert_array_equal(data.data,assert_val), f"2D Array with 3 rows and 4 columns failed")


if __name__ == '__main__':
    unittest.main()