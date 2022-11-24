import unittest
from pong import utility
from pong.vector import MCVector
from mcpi import vec3
from pong import input
from .fake_minecraft import Minecraft
import pickle


class MCVectorError(RuntimeError): 
    # used to test for exceptions defined in the input class
    pass

# test cases
class TestInput(unittest.TestCase):
    def testInputSingleBlock(self):
        """
        Tests for TactileInput or RangeInput instances of a single block.  Passes if instance is created     
        start_block(x,y,z)
        end_block(x,y,z)           
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))

        
        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        my_controller = input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.TactileInput)

        my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.RangeInput)

    def testInputBlockLineX(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the x axis. Passes if instance is created
        start_block(x1,y,z)
        end_block(x2,y,z)
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39537,83,39955))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        my_controller = input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.TactileInput)

        my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.RangeInput)

    def testInputBlockLineZ(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the z axis. Passes if instance is created
        start_block(x,y,z1)
        end_block(x,y,z2)
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39956))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        my_controller = input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.TactileInput)

        my_controller = input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input.RangeInput)

    def testInputPlaneXZ(self):

        """
        Tests for TactileInput or RangeInput instances of a plane of blocks along the XZ plane. Passes if instance fails to be create
        start_block(x1,y,z1)
        end_block(x2,y,z2)
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39537,83,39956))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        with self.assertRaises(RuntimeError):
            input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)


    def testInputBlockLineY(self):

        """
        Tests for TactileInput or RangeInput instances of a line of blocks along the Y axis. Passes if instance fails to be create
        start_block(x,y1,z)
        end_block(x,y2,z)
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39955))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        with self.assertRaises(RuntimeError):
            input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord) 

    def testInputCuboid(self):

        """
        Tests for TactileInput or RangeInput instances of a cuboid of blocks. Passes if instance fails to be create
        start_block(x1,y1,z1)
        end_block(x1,y2,z2)
        """
        start_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,83,39955))
        end_coord = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,84,39956))

        my_file= open( "server.pkl", "rb" ) 
        server_ip, server_port = pickle.load(my_file)
        my_file.close()
        mc = Minecraft.create(server_ip,server_port)
        with self.assertRaises(RuntimeError):
            input.TactileInput([mc],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input.RangeInput([mc],start_coord=start_coord, end_coord=end_coord)  

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