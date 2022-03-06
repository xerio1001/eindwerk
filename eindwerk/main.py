import turtle

s = turtle.getscreen()
turtle.title("Draw Polygons")
t = turtle.Turtle()
t.reset()


class Dots:
    def __init__(self, x:int, y:int, thickness:int, color:str):
        self.x = x
        self.y = y
        self.thickness = thickness
        if(self.isValidColor(color)):
            self.color = color.lower()
        else:
            raise ValueError(f'You need to pick a color within the range of RGB values (red, green, blue) or black')

    def isValidColor(self, color):
        color = color.lower()
        if(color == "red" or color == "green" or color == "blue" or color == "black"):
            return True
        else:
            return False
        

    def reLocate(self):
        pass

    def reSize(self):
        return NotImplemented


class Triangle(Dots):
    pass


class Rectangle(Dots):
    pass

class Square(Dots):
    pass


class Polygon(Dots):
    pass
