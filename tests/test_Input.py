import unittest
from pong import utility
from pong.vector import MCVector
from mcpi import vec3
from pong import input_object
import os
if int(os.environ['MC_Live_Connection'])==1:
    from mcpi.minecraft import Minecraft
    print("importing real MC")
else:
    from .mock_minecraft import Minecraft
    print("importing fame MC")

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
        scanner = input_object.InputScanner([mc])

        
        my_controller = input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.TactileInputParser)

        my_controller = input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.RangeInputParser)
        mc.conn.socket.close()

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
        scanner = input_object.InputScanner([mc])
        my_controller = input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.TactileInputParser)

        my_controller = input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.RangeInputParser)
        mc.conn.socket.close()
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
        scanner = input_object.InputScanner([mc])

        my_controller = input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.TactileInputParser)

        my_controller = input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        self.assertIsInstance(my_controller, input_object.RangeInputParser)
        mc.conn.socket.close()
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
        scanner = input_object.InputScanner([mc])

        with self.assertRaises(RuntimeError):
            input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        mc.conn.socket.close()

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
        scanner = input_object.InputScanner([mc])
        
        with self.assertRaises(RuntimeError):
            input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord) 
        mc.conn.socket.close()

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
        scanner = input_object.InputScanner([mc])

        with self.assertRaises(RuntimeError):
            input_object.TactileInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)
        
        with self.assertRaises(RuntimeError):
            input_object.RangeInputParser([mc],[scanner],start_coord=start_coord, end_coord=end_coord)  
        mc.conn.socket.close()


if __name__ == '__main__':
    unittest.main()