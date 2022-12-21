# mcpi_pong

This is an absolutely silly project...

A simple pong game for mcpi rendered against a screen of blocks in Minecraft.  This is built to be used with mcpi (https://github.com/martinohanlon/mcpi). 
Players move along strips of blocks in Minecraft to control paddles on a screen rendered in Minecraft for a simple game of pong.  This project creates a basic graphics engine for 2d rasterization of colored wool blocks in MineCraft.  The engine consists of a screen with two virtual pages, and optimized page-flipping so only changed pixels are rendered.

<h3>Prerequisites</h3>
You must have access to a Minecraft server running spigotmc (https://www.spigotmc.org/).  You can run this against localhost, but you'll need a buddy to join your server for a two-player game

<h3>Installation</h3>
1. This repository contains submodules, in order to correctly clone use <code>git clone --recurse-submodules git@github.com:DaveGuenther/mcpi_pong.git</code>.<br>
2. Install necessary python package dependencies (including mcpi)<br>
<code>make install</code><br><br>
3. Once packages are installed, you must let the software know where to find your minecraft server<br>
<code>python config-server.py</code><br>
This script will prompt you for your server ip address (you can also use 'localhost') and mcpi port (default is 4711).  Once complete, the script will save this information to a <code>server.pkl</code> file used by the main program to connect to the server.<br>

<h3>Executing Unit Tests</h3>
This project uses the unittest module to perform unit testing across all objects.  However, some objects require a live MC Server connection (the Minecraft class) in order to execute.  This includes objects that place blocks in the MC World, get Player information from the MC World, or get Block data from the MC World.  There are also a number of class objects that pass through an instance of a Minecraft class object.  The Minecraft class itself must be instantiated with server information and will provide an error if the connection fails. 

For testing purposes, I've created a fake-minecraft class in the tests/ folder that is invoked when you want to use it in the various test scripts.  You can control whether to invoke the fake-minecraft class from the makefile as follows:
- <code>make test</code> will run all unit tests using the mcpi.minecraft.Minecraft class and expects that you have a valid server.pkl file created.
- <code>make test-dry</code> will run all unit tests using the fake-minecraft.Minecraft class.  It will not connect to any server and only holds enough objects/attributes to mimic server functionality for test code behavior.  For example, if setting blocks, instead of setting them in the real MC world, it will simply print to the console for each block set, the X,Y,Z coordinate and blick type.

<h3>Running Pong</h3>
Once you have configured your server.pkl file, you can start the pong game on your server by running <code>python main.py</code>.  Players on yor server should visit the following Minecraft location to see the pong structures built (39524, 88, 39962).

Pong is a 2 player game.  Each controller also has a loading block at the top that registers the player's ID with the controller during gameplay.  This loading block will flash between black and the player's color.  Both players need to stand on their loading blocks in order to begin.  When both players are standing on their loading blocks, the blocks will disappear and they'll drop into the controller.  Once in the controller, each player will be standing on a colored strip of blocks.  This strip works like a joystick.  Walking right will move that player's paddle to the right.  Walking left will move that player's paddle to the left.  Spin can be applied to the ball during collision if the controller is moving left or right at the time that the collision with a ball occurs.

There is a safety net built in where if for some reason the screen edges fail to register a collision with the ball and it flies off screen, the game will reset if a ball hasn't collided with an edge for at least 10 seconds.






