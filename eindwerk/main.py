from math import sin, cos, radians
import turtle

turtle.title("Draw Polygons")
t = turtle.Turtle()

class Dots:
    def __init__(self, x:int, y:int):
        if type(x) is not int:
            raise TypeError(f'The value of the x variable is not an integer. {x}')
        else:
            self.x = x
        
        if type(y) is not int:
            raise TypeError(f'The value of the y variable is not an integer. {y}')
        else:
            self.y = y

    def reLocate(self):
        pass


class Triangle:
    def __init__(self, *args:int):
        self.dots = args

    def isValidColor(self, color):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

    def draw(self, color, thickness, test:bool = False):
        if self.isValidColor(color):
            self.color = color.lower()
        else:
            raise ValueError(f'Give a color within the range of RGB or the color "black".')
        
        if thickness <= 0:
            raise ValueError(f'The thickness of the line cannot be lower than or equal to 0')
        else:
            self.thickness = thickness

        if test == False:
            t.penup()
            t.color(self.color)
            t.pensize(self.thickness)
            for dot in self.dots:
                t.goto(dot.x, dot.y)
                t.pendown()

            t.goto(self.dots[0].x, self.dots[0].y)
        
    def reLocate(self, deltaX:int, deltaY:int):
        self.deltaX = deltaX
        self.deltaY = deltaY

        for dot in self.dots:
            dot.x += self.deltaX
            dot.y += self.deltaY

    def rotate(self, point:tuple, degree:int):
        self.degree = radians(degree)
        for dot in self.dots:
            tempX = dot.x
            tempY = dot.y
            tempX -= point[0]
            tempY -= point[1]
            dot.x = (tempX * cos(self.degree) - tempY * sin(self.degree)) + point[0]
            dot.y = (tempY * cos(self.degree) + tempX * sin(self.degree)) + point[1]
            dot.x = round(dot.x)
            dot.y = round(dot.y)


class Square:
    def __init__(self, *args:int, length:int):
        self.dots = args
        self.length = length
        self.getCorners()

    def getCorners(self):
        p1 = self.dots[0] # Example: Bottom left
        p2 = Dots(p1.x + self.length, p1.y) # Example: Bottom right
        p3 = Dots(p1.x + self.length, p1.y + self.length) # Example: Top right
        p4 = Dots(p1.x, p1.y + self.length) # Example: Top left

        self.dots = list(self.dots)
        self.dots.clear()
        self.dots.extend((p1, p2, p3, p4))

    def isValidColor(self, color:str):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

    def draw(self, color:str, thickness:int):
        if self.isValidColor(color):
            self.color = color.lower()
        else:
            raise ValueError(f'Give a color within the range of RGB or the color "black".')
        
        if thickness <= 0:
            raise ValueError(f'The thickness of the line cannot be lower than or equal to 0')
        else:
            self.thickness = thickness

        t.color(self.color)
        t.pensize(self.thickness)
        for dot in self.dots:
            t.goto(dot.x, dot.y)
            t.pendown()
        t.goto(self.dots[0].x, self.dots[0].y)

    def reSize(self):
        pass


class Rectangle:
    def __init__(self, *args:int, length:int, height:int):
        self.dots = args
        self.length = length
        self.height = height
        self.getCorners()

    def getCorners(self):
        p1 = self.dots[0] # Example: Bottom left
        p2 = Dots(p1.x + self.length, p1.y) # Example: Bottom right
        p3 = Dots(p1.x + self.length, p1.y + self.height) # Example: Top right
        p4 = Dots(p1.x, p1.y + self.height) # Example: Top left

        self.dots = list(self.dots)
        self.dots.clear()
        self.dots.extend((p1, p2, p3, p4))        

    def isValidColor(self, color:str):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

    def draw(self, color:str, thickness:int):
        if self.isValidColor(color):
            self.color = color.lower()
        else:
            raise ValueError(f'Give a color within the range of RGB or the color "black".')
        
        if thickness <= 0:
            raise ValueError(f'The thickness of the line cannot be lower than or equal to 0')
        else:
            self.thickness = thickness

        t.color(self.color)
        t.pensize(self.thickness)
        t.penup()
        for dot in self.dots:
            t.goto(dot.x, dot.y)
            t.pendown()
        t.goto(self.dots[0].x, self.dots[0].y)



class Polygon:
    def __init__(self, *args:int):
        self.dots = args

    def isValidColor(self, color:str):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

    def draw(self, color:str, thickness:int):
        if self.isValidColor(color):
            self.color = color.lower()
        else:
            raise ValueError(f'Give a color within the range of RGB or the color "black".')
        
        if thickness <= 0:
            raise ValueError(f'The thickness of the line cannot be lower than or equal to 0')
        else:
            self.thickness = thickness

        t.color(self.color)
        t.pensize(self.thickness)
        t.penup()
        for dot in self.dots:
            t.goto(dot.x, dot.y)
            t.pendown()
        t.goto(self.dots[0].x, self.dots[0].y)

#turtle.mainloop()

"""
In het tekenprogramma is het de bedoeling dat men punten kan plaatsen.
En willekeurige veelhoeken kan tekenen door meerdere punten te plaatsen. Alle veelhoeken hebben een lijndikte en kleur. Deze worden gebruikt in de draw method.
Rechthoeken kan tekenen door 1 punt te plaatsen en een hoogte en breedte mee te geven.  Of door 2 punten te tekenen.
Driehoeken kan tekenen.
En vierkanten kan tekenen door 1 punt en een lengte mee te geven.

Alles kan verplaatst worden door een verplaatsing in de x en y richting mee te geven.
Rechthoeken en vierkanten kunnen resized worden door een hoekpunt te verslepen. Dit doe je door het oud hoekpunt en het nieuwhoek punt mee te geven.  Tip: Hier kan je hoekpunten vergelijken met == bijv.
Alles kan geroteerd worden door een punt mee te geven en een hoek in graden. Dit zorgt voor een rotatie van je veelhoek/punt met die bepaalde hoek rond dat punt.
"""