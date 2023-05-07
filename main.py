from gcodeparser import GcodeParser
import turtle

turtle.setworldcoordinates(0, 0, 700, 700)
turtle.speed(100000000)

gcodeFile = input("what is the name of the gcode file?")

with open(gcodeFile, 'r') as f:
    gcode = f.read()

parsedGcode = GcodeParser(gcode).lines




def getLayer(Gcode, layer):
    if layer == 0:
        return int(0)
    currentLayer = 0
    for i in range(0, len(parsedGcode)):
        if type(Gcode[i].get_param("Z")) == float:
            if Gcode[i].get_param("Z") > 0:
                currentLayer += 1
                if currentLayer == layer:
                    return i + 1
                
def drawLayer(Layer, parsedGcode, scale):
    turtle.pendown()
    for i in range(getLayer(parsedGcode, Layer) , getLayer(parsedGcode, Layer + 1)):
            if parsedGcode[i].command == ('G', 0):
                turtle.color("red")
                if parsedGcode[i].command[0] == "G" and "X" in parsedGcode[i].params and "Y" in parsedGcode[i].params:
                    turtle.setpos(parsedGcode[i].get_param("X", return_type=float) * scale, parsedGcode[i].get_param("Y", return_type=float) * scale)
                turtle.color("black")
            else:
                if parsedGcode[i].command[0] == "G" and "X" in parsedGcode[i].params and "Y" in parsedGcode[i].params:
                    turtle.setpos(parsedGcode[i].get_param("X", return_type=float) * scale, parsedGcode[i].get_param("Y", return_type=float) * scale)
        


while True:
    Layer = int(input("which layer do you want to see?"))
    Scale = int(input("what scale do you want to see it at?"))
    turtle.clear()

    drawLayer(Layer, parsedGcode, Scale)

