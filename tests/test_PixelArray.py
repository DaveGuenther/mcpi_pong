import unittest
import numpy as np
from pong.utility import PixelArray


class TestPixelArray(unittest.TestCase):
    def test_2x2array(self):
        data = PixelArray(3, 4)
        assert_val=np.array(
            [
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val), f"2D Array with 3 rows and 4 columns failed")

    def test_4x1array(self):
        data = PixelArray(4, 1)
        assert_val=np.array(
            [
                [0,0,0,0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val))
    def test_1x4array(self):
        data = PixelArray(1, 4)
        assert_val=np.array(
            [
                [0],
                [0],
                [0],
                [0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val))
    def test_0x1array(self):
        data = PixelArray(0, 1)
        assert_val=np.array(
            [[]]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val))
    def test_setPoint(self):
        data = PixelArray(3, 3)
        assert_val=np.array(
            [
                [1,0,0],
                [0,2,4],
                [0,3,0]
            ]
        )
        data.setPoint(0,0,1)
        data.setPoint(1,1,2)
        data.setPoint(2,1,4)
        data.setPoint(1,2,3)

        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val))
    
    def test_getPoint(self):
        data = PixelArray(3, 3)
        assert_val=np.array(
            [
                [1,0,0],
                [0,2,4],
                [5,3,0]
            ]
        )
        data.data=assert_val
        self.assertEqual(data.getPoint(0,2),5)
        self.assertEqual(data.getPoint(2,1),4)
        self.assertEqual(data.getPoint(0,0),1)

    def test_getWidth(self):
        data = PixelArray(3, 1)

        self.assertEqual(data.getWidth(),3)

    def test_getHeight(self):
        data = PixelArray(33, 100)

        self.assertEqual(data.getHeight(),100)




if __name__ == '__main__':
    unittest.main()