import pickle

server_ip = input("Enter Minecraft Server IP (xxx.xxx.xxx.xxx): ")
server_port = int(input ("Enter mcpi Port: "))
        
pickle.dump((server_ip, server_port),open("server.pkl", "wb" ))
print("Server information stored!")
