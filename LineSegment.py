from pong.line_segment import LineSegment
import numpy as np
from pong.game_object import GameObject
from pong.game_object import Edge


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

A0=np.array([0,0])
A1=np.array([.13864784,.99034175])
B0=np.array([0,-14])
B1=np.array([0,-15])
A = LineSegment(A0,A1) # vert ball
B = LineSegment(B0,B1) # Horizontal
x = A.interceptWith(B)
print(A0-x)
print(A1-x)
print(B0-x)
print(B1-x)


A0=np.array([2,2])
A1=np.array([1,-2])
B0=np.array([2,1])
B1=np.array([-1,-2])
A = LineSegment(A0,A1) # vert ball
B = LineSegment(B0,B1) # Horizontal
x = A.interceptWith(B)
print(A0-x)
print(A1-x)
print(B0-x)
print(B1-x)



A0=np.array([-0.19404463, -12.94044628])
A1=np.array([-.34330021, -14.43300207])
B0=np.array([-8,-13.9])
B1=np.array([-4,-13.9])
ball = LineSegment(A0,A1) # ball
edge = LineSegment(B0,B1) # edge
x = ball.interceptWith(edge)
x = edge.interceptWith(ball)
print(A0-x)
print(A1-x)
print(B0-x)
print(B1-x)


A0=np.array([0,0])
A1=np.array([-0.09950372,-0.99503719])
B0=np.array([-9,17])
B1=np.array([9,17])
ball = LineSegment(A0,A1) # ball
edge = LineSegment(B0,B1) # edge
x = ball.interceptWith(edge)
print(A0-x)
print(A1-x)
print(B0-x)
print(B1-x)

# add to test cases V V V V V
A0=np.array([-1.29354835,-12.93548347])
A1=np.array([-1.39305207,-13.93052066])
B0=np.array([-1.14285714,-13.9])
B1=np.array([2.85714286,-13.9])
ball = LineSegment(A0,A1) # ball
edge = LineSegment(B0,B1) # edge
x = ball.interceptWith(edge)
print(A0-x)
print(A1-x)
print(B0-x)
print(B1-x)