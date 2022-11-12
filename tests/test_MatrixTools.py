import unittest
import numpy as np
import pickle
import math
from pong.matrix_tools import MatrixTools

class TestMatrixTools(unittest.TestCase):
    def testVectorLength(self):
        my_vec = np.array([0,3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertTrue(my_vec_length==3)

        my_vec = np.array([-3,3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertAlmostEqual(my_vec_length, 4.242640687)

        my_vec = np.array([-3,0])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertTrue(my_vec_length==3)

        my_vec = np.array([-3,-3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertAlmostEqual(my_vec_length, 4.242640687)       

        my_vec = np.array([0,-3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertTrue(my_vec_length==3)

        my_vec = np.array([3,-3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertAlmostEqual(my_vec_length, 4.242640687)  

        my_vec = np.array([3,0])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertTrue(my_vec_length==3)

        my_vec = np.array([3,3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        self.assertAlmostEqual(my_vec_length, 4.242640687)  

    def testUnitVector(self):
        my_vec = np.array([0,3])
        my_vec_length = MatrixTools.getVectorLength(my_vec)
        my_vec = MatrixTools.getUnitVector(my_vec)
        self.assertTrue((my_vec==np.array([0,1])).all())
   

    def testRotateVector(self):
        #test 1
        my_vec = np.array([0,3])

        my_vec_length = MatrixTools.getVectorLength(my_vec)
        my_vec = MatrixTools.getUnitVector(my_vec)
        my_vec = MatrixTools.rotateVector(-90.0, my_vec)
        my_vec = my_vec*my_vec_length  

        self.assertAlmostEqual(my_vec[0], 3.0)  
        self.assertAlmostEqual(my_vec[1], 0) 

        #test 2
        my_vec = np.array([0,3])

        my_vec_length = MatrixTools.getVectorLength(my_vec)
        my_vec = MatrixTools.getUnitVector(my_vec)
        my_vec = MatrixTools.rotateVector(0, my_vec)
        my_vec = my_vec*my_vec_length  
        print(round(my_vec[0],3))    
        self.assertAlmostEqual(my_vec[1], 3.0)  
        self.assertAlmostEqual(my_vec[0], 0)          

def testGetOrthogonalForceVector(self):
        my_vec = np.array([0.01,6.01])
        my_force_vec = MatrixTools.getOrthogonalForceVector(my_vec, 1)
        self.assertAlmostEqual(my_force_vec[0], .999998)  
        self.assertAlmostEqual(my_force_vec[1], .001666389)  


if __name__ == '__main__':
    unittest.main()