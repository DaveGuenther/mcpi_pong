from pong.line_segment import LineSegment
import numpy as np

A = LineSegment(np.array([4,2]),np.array([2,4]))
B = LineSegment(np.array([1,2]),np.array([4,4]))

x = A.xInterceptWith(B)
print(x)
if x:
    y=A.getYfromX(x)
    print(y)
