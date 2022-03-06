from multiprocessing.sharedctypes import Value
from eindwerk.main import *
import pytest


def test_validDotConstructor():
    dotsDummy1 = Dots(1, 1, 2, "Red")
    assert dotsDummy1.x == 1 and dotsDummy1.y == 1 and dotsDummy1.thickness == 2 and dotsDummy1.color == "red"
    

def test_invalidColor():
    with pytest.raises(ValueError):
        Dots(1, 1, 2, "Orange")
