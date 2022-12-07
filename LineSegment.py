from pong.line_segment import LineSegment
import numpy as np

A = LineSegment(np.array([4,2]),np.array([2,4]))
B = LineSegment(np.array([1,2]),np.array([4,4]))

x = A.interceptWith(B)
print(x)




A = LineSegment(np.array([-2,4]),np.array([-1,2]))
B = LineSegment(np.array([-3,3]),np.array([2,3]))

x = A.interceptWith(B)
print(x)


A = LineSegment(np.array([-2,2]),np.array([-2,-1])) # Vertical
B = LineSegment(np.array([-1,1]),np.array([-3,1])) # Horizontal

x = A.interceptWith(B)
print(x)


A = LineSegment(np.array([-1,1]),np.array([-3,1])) # Vertical
B = LineSegment(np.array([-2,2]),np.array([-2,-1])) # Horizontal

x = A.interceptWith(B)
print(x)

A = LineSegment(np.array([-2,2]),np.array([-2,-1])) # Vertical
B = LineSegment(np.array([-1,1]),np.array([1,1])) # Horizontal

x = A.interceptWith(B)
print(x)

x = B.interceptWith(A)
print(x)