import unittest
import numpy as np
import pickle
import os
from pong.vector import MCVector
from pong.render import Renderer
from pong.render import PixelArray
from pong.game_object import GameObject
from pong.game_object import Ball
from pong.game_object import Rectangle
from pong.event import EndEvent

if int(os.environ['MC_Live_Connection'])==1:
    from mcpi.minecraft import Minecraft
    print("importing real MC")
else:
    from .mock_minecraft import Minecraft
    print("importing fame MC")

class TestGameObjectInterface(unittest.TestCase):
    """
    Tests that instantiating GameObject directly raises a RuntimeError
    """
    def testInstanceGameObject(self):
        self.assertRaises(RuntimeError, lambda:GameObject())

    def testBallObject(self):
        """
        Tests instantiation of Ball object
        """
        # connect to active server
        server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
        mc = Minecraft.create(server_ip,server_port)

        #Initialize subsystems
        top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display..  Display is facing west
        painter = Renderer([mc], top_left_screen_coord, 16,32,type='cart') 

        # Initialize Ball
        start_pos = np.array([0,0])
        start_direction = np.array([0,1])
        ball_speed=1
        end_event = EndEvent()
        ball1 = Ball([painter], [end_event], start_pos, start_direction, ball_speed, -.1, 2)

        self.assertIsInstance(ball1, Ball, f"Painter class failed to initialize")
        mc.conn.socket.close()


#class TestRectangle(unittest.TestCase):
#    """
#    Tests the concrete clipping rectangle class of game object used by paddles and screen edges.  We'll test a number of collision cases and check the resulting ball position and trajectory.
#    """
#    def testHorizontalEdgeCollosion(self):
        

if __name__=='__main__':
    unittest.main()