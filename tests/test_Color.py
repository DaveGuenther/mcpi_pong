import unittest
import numpy as np
from pong.render import Color

class TestColor(unittest.TestCase):
    def test_getColor(self):

        assert_val=(35,15)
        self.assertTrue(Color.get(0),assert_val)

if __name__ == '__main__':
    unittest.main()