from multiprocessing.managers import ValueProxy
from eindwerk.main import *
import pytest

#################### Dots Class Tests ####################

@pytest.fixture
def dotDummy1():
    """Creates a dummy for dots with correct values."""
    return Dots(10, 20)
    

def test_isValidDotsConstructor(dotDummy1):
    dotDummy1
    assert (
    dotDummy1.x == 10 
    and dotDummy1.y == 20
    )


@pytest.mark.parametrize(("x", "y"),[
    ("1", 2),
    (1, "2"),
    ("1", "2")
])
def test_isInvalidDotsConstructor(x, y):
    with pytest.raises(TypeError):
        Dots(x, y)

#################### Triangle Class Tests ####################

@pytest.fixture
def triangleDummy1():
    """creates a dummy for triangle with correct values."""
    p1 = Dots(10, 20)
    p2 = Dots(30, 40)
    p3 = Dots(50, 20)
    return Triangle(p1, p2, p3)

def test_isValidTriangleConstructor(triangleDummy1):
    assert triangleDummy1.dots[0].x == 10 and triangleDummy1.dots[0].y == 20
    assert triangleDummy1.dots[1].x == 30 and triangleDummy1.dots[1].y == 40
    assert triangleDummy1.dots[2].x == 50 and triangleDummy1.dots[2].y == 20


def test_areValidArguments(triangleDummy1):
    triangleDummy1.draw("blue", 5, True)
    assert (
    triangleDummy1.color == "blue" 
    and triangleDummy1.thickness == 5 
    )


@pytest.mark.parametrize(("color", "thickness"),[
    ("orange", 5),
    ("white", 3)
])
def test_isInvalidColor(triangleDummy1, color, thickness):
    with pytest.raises(ValueError):
        triangleDummy1.draw(color, thickness)


@pytest.mark.parametrize(("color", "thickness"),[
    ("red", -2),
    ("Blue", 0),
])
def test_correctValueOfThickness(triangleDummy1, color, thickness):
    with pytest.raises(ValueError):
        triangleDummy1.draw(color, thickness)

#################### Square Class Tests ####################

@pytest.fixture
def squareDummy1():
    """creates a dummy for square with correct values."""
    p1 = Dots(10, 20)
    return Square(p1, length = 20)


def test_isValidSquareConstructor(squareDummy1):
    assert (
    squareDummy1.dots[0].x == 10 
    and squareDummy1.dots[0].y == 20 
    and squareDummy1.length == 20
    )


def test_isValidColorAndThick(squareDummy1):
    squareDummy1.draw("Red", 2)
    assert (
    squareDummy1.color == "red" 
    and squareDummy1.thickness == 2
    )


@pytest.mark.parametrize(("color", "thickness"),[
    ("Orange", 2),
    ("white", 5)
])
def test_isInvalidColor(squareDummy1, color, thickness):
    with pytest.raises(ValueError):
        squareDummy1.draw(color, thickness)


@pytest.mark.parametrize(("color", "thickness"),[
    ("red", -7),
    ("Green", 0)
])
def test_isInvalidThickness(squareDummy1, color, thickness):
    with pytest.raises(ValueError):
        squareDummy1.draw(color, thickness)

#################### Rectangle Class Tests ####################

@pytest.fixture
def rectangleDummy1():
    """creates a dummy for rectangle with correct values."""
    p1 = Dots(10, 20)
    return Rectangle(p1, length = 20, height = 40)


def test_isValidRectangleConstructor(rectangleDummy1):
    assert ( 
    rectangleDummy1.dots[0].x == 10 
    and rectangleDummy1.dots[0].y == 20 
    and rectangleDummy1.length == 20 
    and rectangleDummy1.height == 40
    )


def test_isValidColorAndThickRectangle(rectangleDummy1):
    rectangleDummy1.draw("Red", 2)
    assert (
    rectangleDummy1.color == "red" 
    and rectangleDummy1.thickness == 2
    )


@pytest.mark.parametrize(("color", "thickness"),[
    ("Orange", 2),
    ("white", 5)
])
def test_isInvalidColorRectangle(rectangleDummy1, color, thickness):
    with pytest.raises(ValueError):
        rectangleDummy1.draw(color, thickness)


@pytest.mark.parametrize(("color", "thickness"),[
    ("red", -7),
    ("Green", 0)
])
def test_isInvalidThicknessRectangle(rectangleDummy1, color, thickness):
    with pytest.raises(ValueError):
        rectangleDummy1.draw(color, thickness)

#################### Polygon Class Tests ####################

@pytest.fixture
def polygonDummy1():
    """creates a dummy for rectangle with correct values."""
    p1 = Dots(70, 60)
    p2 = Dots(40, 40)
    p3 = Dots(50, 10)
    p4 = Dots(90, 10)
    p5 = Dots(90, 40)
    return Polygon(p1, p2, p3, p4, p5)


def test_isValidPolygonConstructor(polygonDummy1):
    assert polygonDummy1.dots[0].x == 70 and polygonDummy1.dots[0].y == 60
    assert polygonDummy1.dots[1].x == 40 and polygonDummy1.dots[1].y == 40
    assert polygonDummy1.dots[2].x == 50 and polygonDummy1.dots[2].y == 10
    assert polygonDummy1.dots[3].x == 90 and polygonDummy1.dots[3].y == 10
    assert polygonDummy1.dots[4].x == 90 and polygonDummy1.dots[4].y == 40


def test_areValidArgumentsPoly(polygonDummy1):
    polygonDummy1.draw("blue", 5)
    assert (
    polygonDummy1.color == "blue" 
    and polygonDummy1.thickness == 5 
    )


@pytest.mark.parametrize(("color", "thickness"),[
    ("orange", 5),
    ("white", 3)
])
def test_isInvalidColorPolygon(polygonDummy1, color, thickness):
    with pytest.raises(ValueError):
        polygonDummy1.draw(color, thickness)


@pytest.mark.parametrize(("color", "thickness"),[
    ("red", -2),
    ("Blue", 0),
])
def test_correctValueOfThicknessPolygon(polygonDummy1, color, thickness):
    with pytest.raises(ValueError):
        polygonDummy1.draw(color, thickness)
