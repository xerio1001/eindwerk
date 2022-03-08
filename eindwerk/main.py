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
    def __init__(self, *args):
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


class Square:
    def __init__(self, *args, length):
        self.dots = args
        self.length = length
        self.getCorners()

    def isValidColor(self, color):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

    def getCorners(self):
        p1 = self.dots[0] # Example: Bottom left
        p2 = Dots(p1.x + self.length, p1.y) # Example: Bottom right
        p3 = Dots(p1.x + self.length, p1.y + self.length) # Example: Top right
        p4 = Dots(p1.x, p1.y + self.length) # Example: Top left

        self.dots = list(self.dots)
        self.dots.clear()
        self.dots.extend((p1, p2, p3, p4))

    def draw(self, color, thickness):
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
    def __init__(self, *args):
        self.dots = args

    def reSize(self):
        pass


class Polygon:
    def __init__(self):
        pass

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