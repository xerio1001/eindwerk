class Dots:
    def __init__(self, x:int, y:int, thickness:int, color:str):
        self.x = x
        self.y = y
        self.thickness = thickness
        self.color = color

    def reLocate(self):
        pass

    def reSize(self):
        return NotImplemented


class Triangle(Dots):
    pass


class Rectangle(Dots):
    pass


class Triangle(Dots):
    pass


class Polygon(Dots):
    pass
