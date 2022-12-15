import numpy as np
from mcpi.minecraft import Minecraft
import pickle
from pong.line_segment import LineSegment
from pong.game_object import Rectangle
from pong.game_object import Ball
from pong.game_object import Edge
from pong.matrix_tools import MatrixTools

def getReflectedRay(ball_screen, edge_screen, intercept):
    pass

ball_screen=LineSegment(np.array([1,-1]),np.array([-2,2]),directional=True)
edge_screen=LineSegment(np.array([-1,2]),np.array([-1,-2]))
intercept = np.array([-1,1])

#subtract intercept from both secments
origin_ball=LineSegment(ball_screen.getPoints()[0]-intercept, ball_screen.getPoints()[1]-intercept)
origin_edge=LineSegment(edge_screen.getPoints()[0]-intercept, edge_screen.getPoints()[1]-intercept)

if edge_screen.getSlope()=='vertical':
    #rotate ball by -90 deg
    ball_vec_end_in_edge_space = MatrixTools.rotateVector(-90, origin_ball.getPoints()[1])
    print(ball_vec_end_in_edge_space)
elif edge_screen.getSlope()==0:
    pass
else:
    #slope is either positive or negative but not vertical or horizontal
    pass