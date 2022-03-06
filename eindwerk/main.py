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
        self.color = color.lower()

    def pickColor(self):
        if(self.color == "red"):
            t.color = "red"
        elif(self.color == "green"):
            t.color = "green"
        elif(self.color == "blue"):
            t.color = "blue"
        elif(self.color == "black"):
            t.color = "black"
        else:
            raise ValueError(f'You need to pick a color in the RGB range or black. (red, green, blue)')

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
