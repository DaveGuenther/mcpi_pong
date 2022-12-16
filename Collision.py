import numpy as np
from mcpi.minecraft import Minecraft
import pickle
import math
from pong.line_segment import LineSegment
from pong.game_object import Rectangle
from pong.game_object import Ball
from pong.game_object import Edge
from pong.matrix_tools import MatrixTools

def getReflectedRay(ball_screen, edge_screen, intercept):
    #subtract intercept from both secments
    origin_ball=LineSegment(ball_screen.getPoints()[0]-intercept, ball_screen.getPoints()[1]-intercept, directional=True)
    origin_edge=LineSegment(edge_screen.getPoints()[0]-intercept, edge_screen.getPoints()[1]-intercept)

    if edge_screen.getSlope()=='vertical':
        #rotate ball by -90 deg
        ball_vec_end_in_edge_space = MatrixTools.rotateVector(-90, origin_ball.getPoints()[1])
        
        #flip y coord of ball endpoint
        ball_vec_end_in_edge_space[1]=ball_vec_end_in_edge_space[1]*-1

        #rotate ball by 90 deg
        new_ball_end_in_screen_space = MatrixTools.rotateVector(90, ball_vec_end_in_edge_space)

    elif edge_screen.getSlope()==0:
        
        #flip y coord of ball endpoint
        new_ball_end_in_screen_space=origin_ball.getPoints()[1]
        new_ball_end_in_screen_space[1]=new_ball_end_in_screen_space[1]*-1    
        
    else:
        #slope is either positive or negative but not vertical or horizontal
        
        #use a non-zero edge point
        edge_point_to_calc_theta=0
        if (origin_ball.getPoints()[0][0]==0)|(origin_ball.getPoints()[0][1]==0):
            edge_point_to_calc_theta=1
        
        #calculate negative theta form edge point
        neg_theta = -1*(180/math.pi)*math.atan(
            float(origin_edge.getPoints()[edge_point_to_calc_theta][1])/
            float(origin_edge.getPoints()[edge_point_to_calc_theta][0]))

        #Rotate ball by neg_theta
        ball_vec_end_in_edge_space = MatrixTools.rotateVector(neg_theta, origin_ball.getPoints()[1])

        #Flip y coord of ball endpoint
        ball_vec_end_in_edge_space[1]=ball_vec_end_in_edge_space[1]*-1

        #rotate ball by pos_theta
        pos_theta = neg_theta*-1
        new_ball_end_in_screen_space = MatrixTools.rotateVector(pos_theta, ball_vec_end_in_edge_space)             


    #add intercept to ball_vec
    reflected_ball_vec = LineSegment(intercept, new_ball_end_in_screen_space+intercept,directional=True)
    return reflected_ball_vec


ball_screen=LineSegment(np.array([1,-1]),np.array([-2,2]),directional=True)
edge_screen=LineSegment(np.array([-1,2]),np.array([-1,-2]))
intercept = np.array([-1,1])

vert_reflected_ray = getReflectedRay(ball_screen, edge_screen, intercept)


hor_case_ball_screen = LineSegment(np.array([2,2]),np.array([-2,-1]),directional=True)
hor_case_edge_screen = LineSegment(np.array([-2,0]),np.array([2,0]))
hor_case_intercept = np.array([-0.5,0])

hor_reflected_ray = getReflectedRay(hor_case_ball_screen, hor_case_edge_screen, hor_case_intercept)

pos_case_ball_screen = LineSegment(np.array([1,-2]),np.array([2,2]),directional=True)
pos_case_edge_screen = LineSegment(np.array([2,2]),np.array([-1,-2]))
pos_case_intercept = np.array([1.5,0.5])

pos_reflected_ray = getReflectedRay(pos_case_ball_screen, pos_case_edge_screen, pos_case_intercept)

neg_case_ball_screen = LineSegment(np.array([0,-1]),np.array([-2,3]),directional=True)
neg_case_edge_screen = LineSegment(np.array([-2,2]),np.array([1,-1]))
neg_case_intercept = np.array([-1,1])

neg_reflected_ray = getReflectedRay(neg_case_ball_screen, neg_case_edge_screen, neg_case_intercept)


print('hello')