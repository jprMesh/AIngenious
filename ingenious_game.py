from helpers import *

class IngeniousGame():
    """Class to facilitate Ingenious game state and mechanics."""

    def __init__(self, players=3):
        """
        Board is stored in axial coordinates.
        The first element of the board address is the axial index.
        The second element is the horizontal index.
                     ___
                 ___/4,2\___
             ___/3,1\___/4,3\___
            /2,0\___/3,2\___/4,4\
            \___/2,1\___/3,3\___/
            /1,0\___/2,2\___/3,4\
            \___/1,1\___/2,3\___/
            /0,0\___/1,2\___/2,4\
            \___/0,1\___/1,3\___/
                \___/0,2\___/
                    \___/
        """
        # Number of hexagons straight across through center
        self.board_size = 7 + 2*players
        self.board = [[0 for y in range(self.board_size)]
                      for x in range(self.board_size)]
        self.outer_rings = players-2
        self.setupBoard()

    def __repr__(self):
        repr_str = ""
        for axial_row in range(self.board_size):
            row = []
            for column in range(self.board_size):
                row.append("{:2}".format(self.board[axial_row][column]))
            repr_str += " ".join(row) + "\n"
        return repr_str

    def setupBoard(self):
        ring_o = self.outer_rings
        center_o = self.board_size//2
        far_side = self.board_size - 1 - self.outer_rings
        self.board[ring_o][ring_o] = Color.r # SW
        self.board[ring_o][center_o] = Color.g # S
        self.board[center_o][ring_o] = Color.b # NW
        self.board[center_o][far_side] = Color.o # SE
        self.board[far_side][far_side] = Color.y # NE
        self.board[far_side][center_o] = Color.p # N

        bound1 = center_o
        bound2 = -center_o
        for axial_row in range(self.board_size):
            for column in range(self.board_size):
                if column > bound1 or column < bound2:
                    self.board[axial_row][column] = -1
            bound1 += 1
            bound2 += 1

    def isValid(self, location):
        if location[0] < 0 or location[1] < 0:
            return False
        if location[0] >= self.board_size or location[1] >= self.board_size:
            return False
        if self.board[location[0]][location[1]] != 0:
            return False
        return True

    def placePiece(self, piece, location, direction):
        l1 = location
        l2 = Loc.add(location, direction)
        c1 = piece.colors[0]
        c2 = piece.colors[1]
        if not (self.isValid(l1) and self.isValid(l2)):
            raise SpotTakenError("Placement invalid.")
        self.board[l1[0]][l1[1]] = c1
        self.board[l2[0]][l2[1]] = c2
        return [self.score(l1, direction), self.score(l2, Dir.Opp(direction))]

    def score(self, location, partner_dir):
        color = self.board[location[0]][location[1]]
        points = 0
        for direction in Dir.All:
            if direction == partner_dir:
                continue
            next_space = Loc.add(location, direction)
            while self.board[next_space[0]][next_space[1]] == color:
                points += 1
                next_space = Loc.add(next_space, direction)
        return [color, points]


if __name__ == '__main__':
    game = IngeniousGame()
    print(game)