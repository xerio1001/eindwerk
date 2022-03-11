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


class FigureFunctions: # Master class
    def __init__(self, *args:int):
        self.dots = args

    def isValidColor(self, color:str):
        color = color.lower()
        if color == "red" or color == "green" or color == "blue" or color == "black":
            return True
        else:
            return False

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

    def reLocate(self, deltaX:int, deltaY:int):
        self.deltaX = deltaX
        self.deltaY = deltaY

        for dot in self.dots:
            dot.x += self.deltaX
            dot.y += self.deltaY

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


class Triangle(FigureFunctions): 
    pass


class Polygon(FigureFunctions):
    pass


class Square (FigureFunctions):
    def __init__(self, *args:int, length:int):
        super().__init__(*args)
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

    def reSize(self, oldDot:tuple, newDot:tuple):
        tempDotX = newDot[0] - oldDot[0]
        tempDotY = newDot[1] - oldDot[1]
        abs(tempDotX)
        abs(tempDotY)
        if(tempDotX == tempDotY):
            for dot in self.dots:
                if(dot.x == oldDot[0]):
                    dot.x = newDot[0]
                if(dot.y == oldDot[1]):
                    dot.y = newDot[1]
        else:
            raise ValueError(f'These values will no longer result in a square.')


class Rectangle(FigureFunctions):
    def __init__(self, *args:int, length:int, height:int):
        super().__init__(*args)
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

    def reSize(self, oldDot:tuple, newDot:tuple):
        for dot in self.dots:
            if(dot.x == oldDot[0]):
                dot.x = newDot[0]
            if(dot.y == oldDot[1]):
                dot.y = newDot[1]

#turtle.mainloop()
