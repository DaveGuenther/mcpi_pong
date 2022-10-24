# mcpi_pong

This is an absolutely silly project...

A simple pong game for mcpi rendered against a screen of blocks in Minecraft.  This is built to be used with mcpi (https://github.com/martinohanlon/mcpi). 
Players move along "paddles" to control ships on a screen rendered in minecraft for a simple game of pong.  This project creates a basic graphics engine for 2d rasterization of colored wool blocks in MineCraft.  The engine consists of a screen with two virtual pages, and optimized page-flipping so only changed pixels are rendered.

<b>Prerequisites</b><br>
You must have access to a Minecraft server running spigotmc (https://www.spigotmc.org/).  You can run this against localhost, but you'll need a buddy to join your server for a two-player game

<b>Installation</b><br>
Install necessary python package dependencies (including mcpi)<br>
<code>make install</code><br><br>

Once packages are installed, you must let the software know where to find your minecraft server<br>
<code>python config-server.py</code><br>
This script will prompt you for your server ip address (you can also use 'localhost') and mcpi port (default is 4711).  Once complete, the script will save this information to a <code>server.pkl</code> file used by the main program to connect to the server.<br>

<b>Running Pong</b><br>
This part is still under construction..  Still trying to draw pixels!  :)






