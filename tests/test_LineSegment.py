import unittest
import numpy as np
from pong.line_segment import LineSegment

# test cases
class TestInput(unittest.TestCase):
    def testInstance(self):
        """
        Test for successful instance of Line Segment given inputs     
        """
        b1 = np.array([4,4])
        b2 = np.array([1,2])

        this_segment = LineSegment(b1, b2)

        self.assertIsInstance(this_segment, LineSegment)

    def testPointOrdering(self):
        """
        Tests for automatic ordering of points when line segment is created such that points increase by x first then by y
        """
        b1 = np.array([4,4])
        b2 = np.array([1,2])

        this_segment = LineSegment(b1, b2)

        p0 = this_segment.getPoints()[0]
        self.assertIsNone(np.testing.assert_array_equal(b2,p0))

    def testIntercept1(self):
        """Segments should intercept"""
        A = LineSegment(np.array([4,2]),np.array([2,4]))
        B = LineSegment(np.array([1,2]),np.array([4,4]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([2.8,3.2])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([2.8,3.2])))

    def testIntercept2(self):
        """Segments should NOT intercept"""
        A = LineSegment(np.array([1,1]),np.array([0,2]))
        B = LineSegment(np.array([2,3]),np.array([2,-2]))

        self.assertFalse(A.interceptWith(B))
        self.assertFalse(B.interceptWith(A))



    def testIntercept3(self):
        """Segments should intercept (1 horizontal)"""
        A = LineSegment(np.array([-2,4]),np.array([-1,2]))
        B = LineSegment(np.array([-3,3]),np.array([2,3]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-1.5,3])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-1.5,3])))


    def testIntercept4(self):
        """Segments should intercept (1 vertical)"""
        A = LineSegment(np.array([-3,3]),np.array([-1,-1]))
        B = LineSegment(np.array([-2,3]),np.array([-2,-2]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2,1])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2,1])))

    def testIntercept5(self):
        """Segments should intercept (1 horizontal)"""
        A = LineSegment(np.array([-2,-1]),np.array([2,-1]))
        B = LineSegment(np.array([-1,-2]),np.array([1,1]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-0.3333333333333333, -1.0])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-0.3333333333333333, -1.0])))


    def testIntercept6(self):
        """Segments should intercept (1 vertical)"""
        A = LineSegment(np.array([-1,0]),np.array([-3,1]))
        B = LineSegment(np.array([-2,-1]),np.array([-2,4]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2, .5])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2, .5])))


    def testIntercept7(self):
        """Segments should intercept (1 vertical AND 1 vertical)"""
        A = LineSegment(np.array([-1,1]),np.array([-3,1]))
        B = LineSegment(np.array([-2,2]),np.array([-2,-1]))

        out_point = A.interceptWith(B)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2, 1])))
        out_point = B.interceptWith(A)
        self.assertIsNone(np.testing.assert_array_equal(out_point,np.array([-2, 1])))

    def testIntercept7(self):
        """Segments should NOT intercept (1 vertical AND 1 vertical)"""
        A = LineSegment(np.array([-1,1]),np.array([-3,1]))
        B = LineSegment(np.array([-2,2]),np.array([-2,4]))

        self.assertFalse(A.interceptWith(B))
        self.assertFalse(B.interceptWith(A))



if __name__ == '__main__':
    unittest.main()