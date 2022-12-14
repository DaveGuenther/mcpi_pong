import unittest
import numpy as np
from pong.render import PixelArray
from pong.game_object import GameObject

class TestGameObjectInterface(unittest.TestCase):
    def testInstanceGameObject(self):
        self.assertRaises(RuntimeError, lambda:GameObject())

if __name__=='__main__':
    unittest.main()