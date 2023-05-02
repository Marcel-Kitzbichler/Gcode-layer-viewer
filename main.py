from gcodeparser import GcodeParser
import turtle

turtle.speed(100)

with open('my_gcode.gcode', 'r') as f:
    gcode = f.read()

for i in range(0, len(moves)):
    turtle.setpos(moves[i]["x"], moves[i]["y"])