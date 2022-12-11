from pong.line_segment import LineSegment
import numpy as np
from pong.game_object import GameObject
from pong.game_object import Wall


def edgeFacingHeading(heading, edge_normal):
    val = np.dot(heading, edge_normal)
    return True if val<0 else False

A = LineSegment(np.array([4,2]),np.array([2,4]))
B = LineSegment(np.array([1,2]),np.array([4,4]))

x = A.interceptWith(B)
print(x)

A = LineSegment(np.array([1,1]),np.array([0,2]))
B = LineSegment(np.array([2,3]),np.array([2,-2]))

x = A.interceptWith(B)
print(x)


A = LineSegment(np.array([-3,3]),np.array([-1,-1]))
B = LineSegment(np.array([-2,3]),np.array([-2,-2]))
x = A.interceptWith(B)
print(x)
x = B.interceptWith(A)
print(x)

A = LineSegment(np.array([-2,-1]),np.array([2,-1]))
B = LineSegment(np.array([-1,-2]),np.array([1,1]))
x = A.interceptWith(B)
print(x)
x = B.interceptWith(A)
print(x)

A = LineSegment(np.array([-1,1]),np.array([-3,1]))
B = LineSegment(np.array([-2,2]),np.array([-2,4]))
x = A.interceptWith(B)
print(x)
x = B.interceptWith(A)
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

###  time to test ball heading/normal faces for collision detection
from pong.matrix_tools import MatrixTools
import numpy as np

A0=np.array([1,-1])
A1=np.array([-1,1])
B0=np.array([-2,2])
B1=np.array([-2,-1])

A = LineSegment(A0,A1) # Diag Ball
B = LineSegment(B0,B1) # Horizontal
A_Heading = MatrixTools.getUnitVector(A1-A0) # heading to edge at 45 degs
B_Normal = MatrixTools.getUnitVector(np.array([3,0])) # facing right

print(A_Heading)
print(B_Normal)
print(edgeFacingHeading(A_Heading, B_Normal))

## Switch ball heading to parallel with edge
A0=np.array([1,-1])
A1=np.array([1,1])
B0=np.array([-2,2])
B1=np.array([-2,-1])

A = LineSegment(A0,A1) # vert ball
B = LineSegment(B0,B1) # Horizontal
A_Heading = MatrixTools.getUnitVector(A1-A0) # heading parallel to edge
B_Normal = MatrixTools.getUnitVector(np.array([3,0])) # facing right

print(A_Heading)
print(B_Normal)
print(edgeFacingHeading(A_Heading, B_Normal))



sub_obj=Wall('Dave')
print(sub_obj.getCartPos())
main_obj=GameObject()