from pygame import *

#DISPLAY
width = 1280
height = 720
fps = 60
tilesize = height/10

#GAME
gamequit = 0
map = [
["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"],
["x"," "," "," "," "," "," "," ","x"," "," "," "," "," ","x","x"],
["x"," ","p"," "," "," "," "," "," "," "," "," "," "," "," ","x"],
["x"," "," "," "," "," "," "," ","x"," "," "," "," "," "," ","x"],
["x","x"," "," ","x","x","x","x","x","x","x","x"," ","x","x","x"],
["x"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","x"],
["x"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","x"],
["x"," "," "," "," "," "," ","x","x","x"," "," "," "," "," ","x"],
["x"," "," "," "," "," "," "," "," "," "," "," "," "," "," ","x"],
["x","x","x","x","x","x","x","x","x","x","x","x","x","x","x","x"]
]