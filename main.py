from mcpi.minecraft import Minecraft
from mcpi import vec3
from mcpi import block
from pong.mcpi_block_structure.blockstructure import BlockStructure
import pickle
import math
import numpy as np
import random
from pong.vector import MCVector
from pong.render import Renderer
from pong.render import PixelArray
from pong.game_object import Controller
from pong.game_object import Rectangle
from pong.game_object import PlayerRectangle
from pong.game_object import Ball
from pong.game_object import Edge
from pong.collision import CollisionHandler
from pong import utility
from pong.timer import Delay
from pong.notification import Notification
from pong.event import EndEvent
import time
from pong import input_object

# connect to active server
server_ip, server_port = pickle.load(open( "server.pkl", "rb" ) )
mc = Minecraft.create(server_ip,server_port)

# Load positions for game screen and controllers in Minecraft world
top_left_screen_coord = MCVector.from_MCWorld_XYZ(39562, 106, 39958) # pixel display..  Display is facing west
screen_nw_bot_corner = MCVector.from_MCWorld_XYZ(39562,74,39957) # Monitor(display) Bottom NW Corner
p1_paddle_nw_bot_corner = MCVector.from_MCWorld_XYZ(39522, 87, 39954) # Player 1 paddle
p2_paddle_nw_bot_corner = MCVector.from_MCWorld_XYZ(39522, 87, 39968) # player 2 paddle

paddle1 = BlockStructure(mc)
paddle1.read_from_file("assets/p1_paddle.pkl")
paddle1.set_structure(p1_paddle_nw_bot_corner.get_mcpiVec())

paddle2 = BlockStructure(mc)
paddle2.read_from_file("assets/p2_paddle.pkl")
paddle2.set_structure(p2_paddle_nw_bot_corner.get_mcpiVec())

screen_obj = BlockStructure(mc)
screen_obj.read_from_file("assets/screen.pkl")
screen_obj.set_structure(screen_nw_bot_corner.get_mcpiVec())


#Initialize subsystems
painter = Renderer([mc], top_left_screen_coord, 16,32,type='cart') 
input_scanner = input_object.InputScanner([mc])


### 'in-game' setup

# p1 controller
p1_joystick_start_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 92, 39955))
p1_joystick_end_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 92, 39962))
p1_ready_button_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 96, 39959))

paddles=[]
# define p1 paddle sprite
p1_pos = np.array([0,-13.9])
p1_sprite = PixelArray(np.array(
    [
        [2,2,2,2]
    ]))

p1_paddle = Controller(
    [mc], [input_scanner], [painter], #subsystems as pointers
    paddle1,p1_paddle_nw_bot_corner, #MC World Objects
    p1_joystick_start_block, p1_joystick_end_block, p1_ready_button_block, #MC World block Coords to define virtual input
    p1_sprite, p1_pos, # Screen Sprite and Screen position
    player_number=1 # set player number associated with this controller
)

# define p2 paddle sprite
p2_sprite = PixelArray(np.array(
    [
        [15,15,15,15]
    ]))

p2_pos = np.array([0,14])

# p2 controller
p2_joystick_start_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 92, 39969))
p2_joystick_end_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536, 92, 39976))
p2_ready_button_block = MCVector.from_MCWorld_Vec(vec3.Vec3(39536,96,39973))

p2_paddle = Controller(
    [mc], [input_scanner], [painter], #subsystems as pointers
    paddle2,p2_paddle_nw_bot_corner, #MC World Objects
    p2_joystick_start_block, p2_joystick_end_block, p2_ready_button_block, #MC World block Coords to define virtual input
    p2_sprite, p2_pos, # Screen Sprite and Screen position
    player_number=2 # set player number asociated with this controller
)
paddles = paddles+[p1_paddle, p2_paddle]
# define EndGame event
end_game_event = EndEvent()

### 'setup' game state initialization

#initialize notification sprites

p1_waiting = Notification([painter],np.array([3,-8]),'p1_waiting',flashing=True)
p1_loaded = Notification([painter], np.array([3,-6]), 'p1_loaded',flashing=False)
p1_p = Notification([painter],np.array([-8,-8]),'P')
p1_1 = Notification([painter],np.array([-2,-8]),'1')

p2_waiting = Notification([painter],np.array([3,16]),'p2_waiting',flashing=True)
p2_p = Notification([painter],np.array([-8,16]),'P')
p2_2 = Notification([painter],np.array([-3,16]),'2')
p2_loaded = Notification([painter], np.array([3,16]), 'p2_loaded',flashing=False)
python_logo = Notification([painter],np.array([-6,7]),'python')

### 'setup-transition-game' setup

start_pos = np.array([0,0])
#start_direction = np.array([-.1,-1])
ball_speed=1
balls=[]
start_direction = np.array(
    [
        (random.uniform(.5, 1.0)*random.sample([-1,1],1)[0]),
        (random.uniform(.5, 1.0)*random.sample([-1,1],1)[0])
    ]) # randomize the ball direction
balls.append(Ball([painter], end_game_event, start_pos, start_direction, ball_speed, 0,  4))
#balls.append(Ball([painter], np.array([1,-1]), start_direction, ball_speed, 0, 15))


# Initialize Screen Collision Bounding Box
collidable_rectangles = []
collidable_rectangles.append(PlayerRectangle(np.array([-9,17]),np.array([9,16]), [p1_paddle], end_game_event, normal_facing_out=True)) # top edge
collidable_rectangles.append(Rectangle(np.array([-9,17]),np.array([-8,-17]), normal_facing_out=True)) #left edge
collidable_rectangles.append(PlayerRectangle(np.array([-9,-17]),np.array([9,-18]), [p2_paddle], end_game_event, normal_facing_out=True)) # bottom edge
collidable_rectangles.append(Rectangle(np.array([8,17]), np.array([9,-17]),normal_facing_out=True)) # right edge


input_objects = []
movable_objects = []
colliders = []
drawable_in_game_screen_objects=[]

input_objects=input_objects + paddles
movable_objects=balls+paddles
#input_objects=[p1_paddle, p2_paddle]
#movable_objects = [ball1, ball2, p1_paddle, p2_paddle]
colliders = colliders + balls
#colliders = [ball1, ball2]
collidable_rectangles = collidable_rectangles + [p1_paddle.getColliderRect(), p2_paddle.getColliderRect()]
#collidable_rectangles = [screen_top, screen_left, screen_bottom, screen_right, p1_paddle.getColliderRect(), p2_paddle.getColliderRect()]
drawable_in_game_screen_objects = drawable_in_game_screen_objects + balls + paddles
#drawable_in_game_screen_objects = [ball1, ball2, p1_paddle, p2_paddle]
collision_handler = CollisionHandler([colliders], [collidable_rectangles])

game_state='setup'

while 1: # start game loop

    if end_game_event.isBallLost()==True:
        game_state='ball_lost'

    if game_state == 'setup':
        #Scan MC input
        input_scanner.scanMC_Player_Positions() # reads positions of all players on server for query by various controllers
        python_logo.draw()
        #Parse MC Input for each controller based on Scanner Results
        p1_paddle.readScannerInput()
        p2_paddle.readScannerInput()
        p1_p.draw()
        p1_1.draw()
        p2_p.draw()
        p2_2.draw()
        if p1_paddle.getControllerState()=='loaded':

            p1_waiting.removeImage()
            p1_loaded.draw()
        else:

            p1_loaded.removeImage()
            p1_waiting.draw()

        if p2_paddle.getControllerState()=='loaded':

            p2_waiting.removeImage()
            p2_loaded.draw()
        else:
            p2_loaded.removeImage()
            p2_waiting.draw()

        if (p1_paddle.getControllerState()=='loaded'):#&(p2.paddle.getControllerState()=='loaded'):
            #p1_waiting.removeImage()
            #p2_waiting.removeImage()
            p1_paddle.dropIn()
            #p2_paddle.dropIn()
            painter.fillCanvas(0)
            transition_msg='start_countdown'
            msg_3 = Notification([painter], np.array([-2,4]),'3')
            msg_2 = Notification([painter], np.array([-2,4]),'2')
            msg_1 = Notification([painter], np.array([-1,4]),'1')
            second_delay = Delay(1000)
            game_state = 'transition-setup-game'
        

    if game_state == 'transition-setup-game':
        painter.fillCanvas(0)        
        p1_paddle.readScannerInput()
        p2_paddle.readScannerInput()  

        if transition_msg=='start_countdown':
            second_delay.start()
            transition_msg='3'

        if transition_msg=='3':
            msg_3.draw()
            if second_delay.getState()==False:
                transition_msg='2'
                second_delay.start()

        if transition_msg=='2':
            msg_2.draw()
            if second_delay.getState()==False:
                transition_msg='1'
                second_delay.start()     

        if transition_msg=='1':
            msg_1.draw()
            if second_delay.getState()==False: 
                for ball in balls:
                    ball.resetBall()        
                game_state='in_game'      
        #if (p1_paddle.getControllerState()=='ingame'):#&(p2.paddle.getControllerState()=='ingame'):


    if game_state == 'in_game':

        #Parse MC Input for each controller based on Scanner Results
        for input_object in input_objects:
            input_object.readScannerInput()

        #Update object positions
        for movable_object in movable_objects:
            movable_object.updatePos()

        # handle collisions
        collision_handler.testCollisions()
            
        if end_game_event.isEnded()==True:
            game_state='end_game'
            winner = str(end_game_event.getWinningPlayer())
            delay_5_secs = Delay(5000)
            msg_p = Notification([painter], np.array([-5,7]),'P',flashing=True)
            msg_player = Notification([painter], np.array([1,7]),winner,flashing=True)
            msg_win = Notification([painter], np.array([-7,-3]),'WIN',flashing=True)
            delay_5_secs.start()
        else:
            #clear canvas
            painter.fillCanvas(0)
            
            #place sprites
            for drawable_object in drawable_in_game_screen_objects:
                drawable_object.draw()
    
    if game_state=='end_game':
        painter.fillCanvas(0)
        if delay_5_secs.getState()==True:
            msg_p.draw()
            msg_player.draw()
            msg_win.draw()

        else: # reset game
            painter.flipVirtualPage()
            painter.fillCanvas(0)
            paddle1.set_structure(p1_paddle_nw_bot_corner.get_mcpiVec())
            paddle2.set_structure(p2_paddle_nw_bot_corner.get_mcpiVec())
            screen_obj.set_structure(screen_nw_bot_corner.get_mcpiVec())
            for controller in input_objects:
                controller.resetController()
            end_game_event.reset()
            game_state='setup'


    if game_state=='ball_lost':
        painter.fillCanvas(0)
        painter.flipVirtualPage()
        painter.fillCanvas(0)
        paddle1.set_structure(p1_paddle_nw_bot_corner.get_mcpiVec())
        paddle2.set_structure(p2_paddle_nw_bot_corner.get_mcpiVec())
        screen_obj.set_structure(screen_nw_bot_corner.get_mcpiVec())
        for controller in input_objects:
            controller.resetController()
        end_game_event.reset()
        game_state='setup'
               

    #show screen
    painter.flipVirtualPage()

print("Hello")
