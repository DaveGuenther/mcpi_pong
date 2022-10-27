import unittest
import numpy as np
from pong.render import PixelArray


class TestPixelArray(unittest.TestCase):
    def test_3x4array(self):
        data = PixelArray.fromDimensions(3, 4)
        assert_val=np.array(
            [
                [0,0,0],
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data.T,assert_val), f"2D Array with 3 rows and 4 columns failed")

    def test_4x1array(self):
        data = PixelArray.fromDimensions(4,1)
        assert_val=np.array(
            [
                [0,0,0,0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data.T,assert_val))

    def test_1x4array(self):
        data = PixelArray.fromDimensions(1, 4)
        assert_val=np.array(
            [
                [0],
                [0],
                [0],
                [0]
            ]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data.T,assert_val))

    def test_0x1array(self):
        data = PixelArray.fromDimensions(0, 1)
        assert_val=np.array(
            [[]]
        )
        self.assertIsNone(np.testing.assert_array_equal(data.data.T,assert_val))

    def test_setPoint(self):
        data = PixelArray.fromDimensions(3, 3)
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
        data = PixelArray.fromDimensions(3, 3)
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
        data = PixelArray.fromDimensions(3, 1)
        self.assertEqual(data.getWidth(),3)

        data = PixelArray.fromDimensions(0,0)
        self.assertEqual(data.getWidth(),0)

        data = PixelArray.fromDimensions(3,0)
        self.assertEqual(data.getWidth(),0)

        data = PixelArray.fromDimensions(0,0)
        self.assertEqual(data.getWidth(),0)

        data = PixelArray(np.array([]))
        self.assertEqual(data.getWidth(),0)        

        data = PixelArray(np.array([[]]))
        self.assertEqual(data.getWidth(),0)  

    def test_getHeight(self):
        data = PixelArray.fromDimensions(33, 100)
        self.assertEqual(data.getHeight(),100)

        data = PixelArray.fromDimensions(0,0)
        self.assertEqual(data.getHeight(),0)

        data = PixelArray.fromDimensions(3,0)
        self.assertEqual(data.getHeight(),0)

        data = PixelArray.fromDimensions(0,3)
        self.assertEqual(data.getHeight(),0)

        data = PixelArray(np.array([]))
        self.assertEqual(data.getHeight(),0)

        data = PixelArray(np.array([[]]))
        self.assertEqual(data.getHeight(),0)  


    def test_fillArray(self):
        data = PixelArray.fromDimensions(5, 5)
        data.fillArray(9)
        assert_val=np.array(
            [
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9],
                [9, 9, 9, 9, 9]                                
            ]
        )

        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val))

    def test_create_PixelArray_from_Array(self):
        
        assert_val=np.array([
            [5, 5, 5, 5, 5],
            [4, 4, 4, 4, 4],
            [3, 3, 3, 3, 3],
            [2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1]
        ])
        data = PixelArray(assert_val)
        


        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val.T))

    def test_filter(self):
        
        initial_array=np.array([
            [5, 5, 5, 5, 5],
            [4, 4, 4, 4, 4],
            [3, 3, 3, 3, 3],
            [2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1]
        ])
        data = PixelArray(initial_array)
        data = data.filter(np.array([True, True, False, False, False]), 0) # filter rows
        data = data.filter(np.array([True, True, True, False, False]),1) # filter columns

        assert_val=np.array([
            [5, 5, 5],
            [4, 4, 4]
        ])

        self.assertIsNone(np.testing.assert_array_equal(data.data,assert_val.T))




if __name__ == '__main__':
    unittest.main()