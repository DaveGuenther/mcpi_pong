import pickle
print("Please be sure that you have the server up and running, and have a player logged into the server for calibration.")
print("You will need to identify that player by his/her name on the server to calibrate.")

server_ip = input("Enter Minecraft Server IP (xxx.xxx.xxx.xxx): ")
server_port = int(input ("Enter mcpi Port: "))
        
pickle.dump((server_ip, server_port),open("server.pkl", "wb" ))
print("Server information stored!  Attempting to connect to server...",end='')

from mcpi.minecraft import Minecraft
from mcpi import vec3
mc = Minecraft.create(server_ip,server_port)
print("Connected!")

player_name = input("Enter name of logged in player to calibrate with: ")
player = mc.getPlayerEntityId(player_name)
player_pos = mc.entity.getTilePos(player)
print("In minecraft, press F3 to see coordinate data of player")
world_x = int(input("Enter x coordinate of this player as shown in Minecraft: "))
world_y = int(input("Enter y coordinate of this player as shown in Minecraft: "))
world_z = int(input("Enter z coordinate of this player as shown in Minecraft: "))


print("")
print("World Vector Position: ("+str(world_x)+", "+str(world_y)+", "+str(world_z)+")")
print("mcpi Vector Position: ("+str(player_pos.x)+", "+str(player_pos.y)+", "+str(player_pos.z)+")")
x_offset = -1*(world_x-player_pos.x)
y_offset = -1*(world_y-player_pos.y)
z_offset = -1*(world_z-player_pos.z)
print("World -> mcpi offset vector: ("+str(x_offset)+", "+str(y_offset)+", "+str(z_offset)+")")
offset_vec = vec3.Vec3(x_offset, y_offset, z_offset)
pickle.dump(offset_vec,open("offset_vector.pkl", "wb" ))

print("Server is cofigured and calibrated!")