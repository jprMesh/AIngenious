class Dir():
    """Directions in axial coordinates."""
    So = [-1,  0]
    SE = [ 0,  1]
    NE = [ 1,  1]
    No = [ 1,  0]
    NW = [ 0, -1]
    SW = [-1, -1]
    All = [So, SE, NE, No, NW, SW]
    
    def Opp(direc):
        return [-x for x in direc]

class Loc():
    """Location."""

    def add(l1, l2):
        return [l1[0] + l2[0], l1[1] + l2[1]]

class Color():
    """Colors."""
    r = 1
    g = 2
    b = 3
    y = 4
    o = 5
    p = 6

class SpotTakenError(Exception):
    """Error for trying to place a piece where one already exists."""
    def __init__(self, message):
        self.message = message

class IngeniousPiece():
    """Piece for Ingenious game."""
    def __init__(self, color1, color2):
        self.colors = [color1, color2]