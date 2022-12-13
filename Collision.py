import numpy as np
from mcpi.minecraft import Minecraft
import pickle
from pong.game_object import Rectangle
from pong.game_object import Ball
from pong.game_object import Edge
from pong.render import Renderer
from pong.vector import MCVector

def edgeFacingHeading(heading, edge_normal):
    val = np.dot(heading, edge_normal)
    return True if val<0 else False

# connect to active server
server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
mc = Minecraft.create(server_ip,server_port)

#Initialize subsystems

top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display..  Display is facing west
painter = Renderer([mc], top_left_screen_coord, 16,32,type='cart') 

# Initialize Balls
start_pos = np.array([0,0])
start_direction = np.array([0,1])
ball_speed=1
ball1 = Ball([painter], start_pos, start_direction, ball_speed, -.1, 2)
ball2 = Ball([painter], start_pos, start_direction, ball_speed, .14, 15)

# Initialize Screen Collision Bounding Box
my_screen_bounds = Rectangle(np.array([-8,16]),np.array([8,-16]),normal_facing_out=False)
dave = np.array([1,0])

colliders = [ball1, ball2]
movable_objects=[ball1, ball2]
collidable_rectangles = [my_screen_bounds]
drawable_screen_objects = [ball1, ball2]

while 1:

    #Scan MC input
    #input_scanner.scanMC_Player_Positions() # reads positions of all players on server for query by various controllers
    
    #Parse MC Input for each controller based on Scanner Results
    #for input_object in input_objects:
    #    input_object.readScannerInput()

    for ball in colliders:
        heading = ball.getHeadingUnitVec()
        for this_rectangle in collidable_rectangles:
            for edge in this_rectangle.getSegments():
                normal = edge.getNormal()
                if edgeFacingHeading(heading, normal):
                    intersection = ball.getHeadingSegment().interceptWith(edge.getSegment())
                    if (type(intersection)!=bool):
                        collider.collide(edge)

    #Update object positions
    for movable_object in movable_objects:
        movable_object.updatePos()
        
    #clear canvas
    painter.fillCanvas(0)
    
    #place sprites
    for drawable_object in drawable_screen_objects:
        drawable_object.draw()
    
    #show screen
    painter.flipVirtualPage()
    #time.sleep(.05)


            